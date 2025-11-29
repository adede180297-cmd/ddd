from datetime import datetime
import random

# ================== NGÀY CỐ ĐỊNH ==================
target_date_tet = datetime(2026, 2, 17)
target_date_noel = datetime(2025, 12, 25)

# ================== TÊN USER ==================
def get_name(update):
    u = update.message.from_user
    return u.first_name or "Bạn"

# ================== CHỌN RANDOM ==================
def pick(data, name):
    msg = random.choice(data)
    return msg.replace("{name}", name)

# ================== MOOD VUI ==================
MOOD_FUNNY = [
    "Hôm nay bot vui dữ lắm luôn á 😆",
    "Bot đang trong mood vui cực mạnh nè 😝",
    "Năng lượng của bot hôm nay: 999% 🌈",
    "Tâm trạng bot đang sáng như ánh mặt trời ☀️",
    "Bot vui quá, muốn chúc bạn thiệt nhiều thứ luôn 😄"
]

# ================== CÂU TẾT ==================
TET_FUNNY = [
    "Chuẩn bị không khí đón xuân nha 🌸",
    "Hy vọng năm mới của bạn thật rực rỡ ✨",
    "Tết này nhớ cười thiệt tươi nha 😄",
    "Xuân đang tới gần từng chút nè 🌼",
    "Chúc bạn sớm cảm nhận được không khí Tết 💛",
]

# ================== CÂU NOEL ==================
NOEL_FUNNY = [
    "Không khí Giáng Sinh đang rất dễ thương nha 🎄",
    "Chúc bạn có mùa Noel thật ấm áp ❤️",
    "Hy vọng bạn nhận được nhiều lời chúc đáng yêu ❄️",
    "Bạn treo đèn Giáng Sinh chưa? ✨",
    "Santa đang chuẩn bị quà đó 😆",
]

# ================== CÂU XUỐNG CA ==================
XUONGCA_FUNNY = [
    "Ráng lên một chút nữa nha 💪",
    "Bạn sắp hết giờ rồi đó 😄",
    "Cố thêm tí nữa, tự do đang tới gần 😆",
    "Nghĩ đến cái giường là có động lực liền 😭",
    "Chúc bạn xuống ca thật nhẹ nhàng ✨",
]

# ================== CÂU LƯƠNG ==================
LUONG_FUNNY = [
    "Ráng chịu đựng nha 😭✌️",
    "Tháng này cố thêm xíu nha 😄",
    "Sắp hết nghèo rồi 😆",
    "Ví bạn sắp được hồi sinh ✨",
    "Hi vọng tháng này không âm 😭",
]

# ================== CÂU ĂN CƠM ==================
ANCOM_FUNNY = [
    "nhớ ăn cơm cho khỏe nha 😄",
    "đừng làm việc mà quên ăn đó nha 🍚",
    "ăn cơm đúng bữa để có sức nha 💪",
    "hôm nay ăn gì ngon chưa? 😆",
    "bụng đói là không vui đâu nha 😭",
]
