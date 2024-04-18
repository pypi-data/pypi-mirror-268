import re
from pathlib import Path

import httpx
from nonebot import get_bot, get_driver, logger, on_command, require
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg
from nonebot.typing import T_State

try:
    import ujson as json
except ModuleNotFoundError:
    import json

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler
from nonebot.plugin import PluginMeta


subscribe = Path(__file__).parent / "subscribe.json"

subscribe_list = json.loads(subscribe.read_text("utf-8")) if subscribe.is_file() else {}


def save_subscribe():
    subscribe.write_text(json.dumps(subscribe_list), encoding="utf-8")


driver = get_driver()


async def get_calendar() -> bytes:
    async with httpx.AsyncClient(http2=True, follow_redirects=False) as client:
        response = await client.get("https://api.vvhan.com/api/zhichang")
        if response.status_code != 302:
            raise ValueError(f"职场日历获取失败，错误码：{response.status_code}")
        image_url = response.headers["location"]
        image = await client.get(image_url)
        return image.content


@driver.on_startup
async def subscribe_jobs():
    for group_id, info in subscribe_list.items():
        scheduler.add_job(
            push_calendar,
            "cron",
            args=[group_id],
            id=f"zhichang_calendar_{group_id}",
            replace_existing=True,
            hour=info["hour"],
            minute=info["minute"],
        )


async def push_calendar(group_id: str):
    bot = get_bot()
    zhichang_img = await get_calendar()
    await bot.send_group_msg(
        group_id=int(group_id), message=MessageSegment.image(zhichang_img)
    )


def calendar_subscribe(group_id: str, hour: str, minute: str) -> None:
    subscribe_list[group_id] = {"hour": hour, "minute": minute}
    save_subscribe()
    scheduler.add_job(
        push_calendar,
        "cron",
        args=[group_id],
        id=f"zhichang_calendar_{group_id}",
        replace_existing=True,
        hour=hour,
        minute=minute,
    )
    logger.debug(f"群[{group_id}]设置职场日历推送时间为：{hour}:{minute}")


zhichang_matcher = on_command("职场日历", aliases={"职场"})


@zhichang_matcher.handle()
async def zhichang(
    event: GroupMessageEvent, matcher: Matcher, args: Message = CommandArg()
):
    if cmdarg := args.extract_plain_text():
        if "状态" in cmdarg:
            push_state = scheduler.get_job(f"zhichang_calendar_{event.group_id}")
            zhichang_state = "职场日历状态：\n每日推送: " + ("已开启" if push_state else "已关闭")
            if push_state:
                group_id_info = subscribe_list[str(event.group_id)]
                zhichang_state += (
                    f"\n推送时间: {group_id_info['hour']}:{group_id_info['minute']}"
                )
            await matcher.finish(zhichang_state)
        elif "设置" in cmdarg or "推送" in cmdarg:
            if ":" in cmdarg or "：" in cmdarg:
                matcher.set_arg("time_arg", args)
        elif "禁用" in cmdarg or "关闭" in cmdarg:
            del subscribe_list[str(event.group_id)]
            save_subscribe()
            scheduler.remove_job(f"zhichang_calendar_{event.group_id}")
            await matcher.finish("职场日历推送已禁用")
        else:
            await matcher.finish("职场日历的参数不正确")
    else:
        zhichang_img = await get_calendar()
        await matcher.finish(MessageSegment.image(zhichang_img))


@zhichang_matcher.got("time_arg", prompt="请发送每日定时推送日历的时间，格式为：小时:分钟")
async def handle_time(
    event: GroupMessageEvent, state: T_State, time_arg: Message = Arg()
):
    state.setdefault("max_times", 0)
    time = time_arg.extract_plain_text()
    if any(cancel in time for cancel in ["取消", "放弃", "退出"]):
        await zhichang_matcher.finish("已退出职场日历推送时间设置")
    match = re.search(r"(\d*)[:：](\d*)", time)
    if match and match[1] and match[2]:
        calendar_subscribe(str(event.group_id), match[1], match[2])
        await zhichang_matcher.finish(f"职场日历的每日推送时间已设置为：{match[1]}:{match[2]}")
    else:
        state["max_times"] += 1
        if state["max_times"] >= 3:
            await zhichang_matcher.finish("你的错误次数过多，已退出职场日历推送时间设置")
        await zhichang_matcher.reject("设置时间失败，请输入正确的格式，格式为：小时:分钟")
