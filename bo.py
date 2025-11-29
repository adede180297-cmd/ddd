from telegram.ext import Application, CommandHandler
from datetime import datetime, timedelta
from random import choice

from config_and_logic import (
    pick, get_name,
    target_date_tet, target_date_noel,
    TET_FUNNY, NOEL_FUNNY, XUONGCA_FUNNY,
    LUONG_FUNNY, ANCOM_FUNNY, MOOD_FUNNY
)

# ================== TOKEN ==================
TOKEN = "8324202114:AAGJM7kfxiKvY5qTqz751elPHz_Prf0otZ8"   # ⚠️ bỏ token bot của bạn vào đây


def mood():
    return choice(MOOD_FUNNY)


# ====================================================================
# ======================== LỆNH TẾT ==================================
# ====================================================================
async def countdown_tet(update, context):
    name = get_name(update)
    now = datetime.now()
    diff = target_date_tet - now

    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "🧨 Đếm ngược đến Tết 2026 nèee! 🧨\n\n"
        f"{mood()}\n"
        f"{name}, {pick(TET_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút {s} giây\n"
        "🌕 Tết rơi vào ngày: 17/02/2026\n"
        "✨ Chúc bạn một năm mới vui tới nóc!"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


# ====================================================================
# ======================== LỆNH NOEL =================================
# ====================================================================
async def countdown_noel(update, context):
    name = get_name(update)
    now = datetime.now()
    diff = target_date_noel - now

    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60

    msg = (
        "🎄 Đếm ngược Noel 2025 nèee! 🎄\n\n"
        f"{mood()}\n"
        f"{name}, {pick(NOEL_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h}
