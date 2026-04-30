import streamlit as st
import os
from datetime import datetime

# 1. CẤU HÌNH HỆ THỐNG & GIAO DIỆN
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", layout="wide")

st.markdown("""
    <style>
    /* Tổng thể nền trắng chữ đen */
    .stApp { background-color: #FFFFFF !important; }
    h1, h2, h3, h4, p, span, div, label, .stMarkdown {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* Nội dung trang sách */
    .noidung-sach {
        background-color: #F8F9FA !important;
        padding: 30px !important;
        border-radius: 12px !important;
        border: 1px solid #D1D5DB !important;
        color: #000000 !important;
        font-size: 20px !important;
        line-height: 1.8 !important;
        text-align: justify !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] { background-color: #F1F5F9 !important; }
    section[data-testid="stSidebar"] * { color: #000000 !important; }
    
    /* FIX TRIỆT ĐỂ Ô CHỌN SÁCH (SELECTBOX) */
    /* 1. Ô hiển thị bên ngoài */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important; 
        border: 2px solid #1E40AF !important; 
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span, div[data-baseweb="select"] div {
        color: #000000 !important;
        font-weight: bold !important;
    }

    /* 2. Danh sách đổ xuống khi nhấn vào (Dropdown Menu) */
    div[data-baseweb="popover"] ul {
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="popover"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        font-weight: normal !important;
    }
    /* Màu khi rê chuột vào từng mục trong danh sách */
    div[data-baseweb="popover"] li:hover {
        background-color: #E2E8F0 !important;
        color: #1E40AF !important;
    }

    /* Định dạng nút bấm */
    .stButton>button {
        background-color: #1E40AF !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border-radius: 8px;
    }
    .stButton>button p, .stButton>button span { 
        color: #FFFFFF !important; 
        -webkit-text-fill-color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU CỐ ĐỊNH (2 tác phẩm đầu)
LIBRARY_DATA = {
    "Ký Ức Vùng Đất Tân Lộc": {
        "Lời mở đầu": """Tân Lộc là vùng đất của phù sa, của cây lành trái ngọt, của những con người chân chất và giàu nghĩa tình...""",
        "Chương 1: Tân Lộc - Vùng đất bồi đắp bởi phù sa": """Tân Lộc thuộc thành phố Cần Thơ, nằm giữa hệ thống sông ngòi chằng chịt của miền Tây Nam Bộ...""",
        "Chương 2: Dấu chân tiền nhân khai phá": """Từ thuở hoang sơ, những người dân đầu tiên đã đến Tân Lộc lập nghiệp...""",
        "Chương 3: Nếp sống và văn hóa Tân Lộc": """Ở Tân Lộc, hàng xóm không chỉ là người ở gần nhau, mà còn là người thân trong những lúc khó khăn...""",
        "Kết luận": """Tân Lộc đẹp không chỉ bởi cây trái sum suê hay dòng sông hiền hòa, mà đẹp bởi con người sống chan hòa, thủy chung và nghĩa tình."""
    },
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng...""",
        "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978...""",
        "Kết luận": """Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."""
    }
}

# 3. TỰ ĐỘNG ĐỌC SÁCH MỚI TỪ THƯ MỤC "TacPham" TRÊN GITHUB
if os.path.exists("TacPham"):
    for ten_sach in os.listdir("TacPham"):
        duong_dan_sach = os.path.join("TacPham", ten_sach)
        if os.path.isdir(duong_dan_sach):
            if ten_sach not in LIBRARY_DATA:
                LIBRARY_DATA[ten_sach] = {}
            
            cac_file = sorted(os.listdir(duong_dan_sach))
            for ten_file in cac_file:
                if ten_file.endswith(".txt"):
                    ten_chuong = ten_file.replace(".txt", "")
                    if "_" in ten_chuong and ten_chuong.split("_")[0].isdigit():
                        ten_chuong = ten_chuong.split("_", 1)[1]
                        
                    with open(os.path.join(duong_dan_sach, ten_file), "r", encoding="utf-8") as f:
                        noidung = f.read()
                    LIBRARY_DATA[ten_sach][ten_chuong] = noidung.replace('\n', '<br>')

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 4. GIAO DIỆN CHÍNH
st.markdown("<h1 style='text-align: center; color: #1E40AF !important;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)

st.sidebar.markdown("## 📖 CHỌN TÁC PHẨM")
selected_book = st.sidebar.selectbox("Chọn cuốn sách bạn muốn đọc:", list(LIBRARY_DATA.keys()))

st.sidebar.markdown("## 📑 MỤC LỤC")
danh_sach_chuong = list(LIBRARY_DATA[selected_book].keys())
if danh_sach_chuong:
    selected_chapter = st.sidebar.radio("Các chương:", danh_sach_chuong)
    
    st.markdown(f"<h3 style='text-align: center; color: #4B5563 !important;'>Tác phẩm: {selected_book}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: #1E40AF !important;'>📌 {selected_chapter}</h2>", unsafe_allow_html=True)
    
    content = LIBRARY_DATA[selected_book][selected_chapter]
    st.markdown(f"<div class='noidung-sach'>{content}</div>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='text-align: center; color: red !important;'>Cuốn sách này đang được cập nhật...</h3>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 5. BÌNH LUẬN
st.markdown("### 💬 Bạn đọc nhận xét")
with st.form("form_comment", clear_on_submit=True):
    name_user = st.text_input("Tên của anh/chị:")
    comment_user = st.text_area("Cảm nhận về tác phẩm này:")
    btn = st.form_submit_button("GỬI BÌNH LUẬN")
    if btn and name_user and comment_user:
        st.session_state.comments.insert(0, {
            "name": name_user, "text": comment_user, "book": selected_book,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

for c in st.session_state.comments:
    if c.get("book") == selected_book:
        st.markdown(f"""
            <div style='background-color: #F3F4F6; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #1E40AF;'>
                <strong style='color: #1E40AF !important;'>👤 {c['name']}</strong> <small>({c['time']})</small><br>
                <p style='color: #000000 !important; margin-top: 5px; text-align: justify;'>{c['text']}</p>
            </div>
        """, unsafe_allow_html=True)
