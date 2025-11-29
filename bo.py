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
        f"⏳ Còn: {days} ngày {h} giờ {m} phút\n"
        "📅 Noel vào ngày: 25/12/2025\n"
        "✨ Chúc bạn mùa lễ tràn ngập niềm vui!"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


# ====================================================================
# ======================= LỆNH XUỐNG CA ===============================
# ====================================================================
async def countdown_xuongca(update, context):
    name = get_name(update)
    now = datetime.now()

    end = now.replace(hour=20, minute=0, second=0, microsecond=0)
    if now > end:
        end += timedelta(days=1)

    diff = end - now

    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "🕗 Đếm ngược đến giờ xuống ca (20:00) nèee! 🕗\n\n"
        f"{mood()}\n"
        f"{name}, {pick(XUONGCA_FUNNY, name)}\n\n"
        f"⏳ Còn: {h} giờ {m} phút {s} giây\n"
        "🏠 Chuẩn bị được về rồi đó!\n"
        "✨ Chúc bạn xuống ca thật nhẹ nhàng!"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


# ====================================================================
# ======================== LỆNH LƯƠNG ================================
# ====================================================================
async def countdown_luong(update, context):
    name = get_name(update)
    now = datetime.now()

    payday = now.replace(day=16, hour=0, minute=0)
    if now > payday:
        payday = payday.replace(month=payday.month % 12 + 1)
        if payday.month == 1:
            payday = payday.replace(year=payday.year + 1)

    diff = payday - now

    days = diff.days
    h = diff.seconds // 3600
    m = (diff.seconds % 3600) // 60
    s = diff.seconds % 60

    msg = (
        "💰 Đếm ngược ngày nhận lương nèee! 💰\n\n"
        f"{mood()}\n"
        f"{name}, {pick(LUONG_FUNNY, name)}\n\n"
        f"⏳ Còn: {days} ngày {h} giờ {m} phút {s} giây\n"
        f"📅 Lương về ngày: {payday.strftime('%d/%m/%Y')}\n"
        "✨ Hy vọng tháng này ví bạn không còn buồn nữa!"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


# ====================================================================
# ========================= LỆNH /ANCOM ===============================
# ====================================================================
async def ancom(update, context):
    name = get_name(update)
    funny = pick(ANCOM_FUNNY, name)

    msg = (
        "🍚 Tới giờ ăn cơm rồi nèeeee! 🍚\n\n"
        f"{mood()}\n"
        f"{name}, {funny}\n"
        "Nhớ đi ăn liền nha, để bụng đói buồn lắm 😭\n"
        "✨ Chúc bạn ăn ngon miệng!"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


# ====================================================================
# ============================== MAIN =================================
# ====================================================================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("countdown", countdown_tet))
    app.add_handler(CommandHandler("noel", countdown_noel))
    app.add_handler(CommandHandler("xuongca", countdown_xuongca))
    app.add_handler(CommandHandler("luong", countdown_luong))
    app.add_handler(CommandHandler("ancom", ancom))

    print("Bot đang chạy…")
    app.run_polling()


if __name__ == "__main__":
    main()
