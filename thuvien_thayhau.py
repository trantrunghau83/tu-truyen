import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH HỆ THỐNG
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    h1, h2, h3, h4, p, span, div, label, .stMarkdown {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* CHỈNH SỬA TẠI ĐÂY: CĂN THẲNG 2 LỀ */
    .noidung-sach {
        background-color: #F8F9FA !important;
        padding: 30px !important;
        border-radius: 12px !important;
        border: 1px solid #D1D5DB !important;
        color: #000000 !important;
        font-size: 20px !important;
        line-height: 1.8 !important;
        text-align: justify !important; /* Lệnh thần thánh để căn thẳng 2 lề */
    }

    section[data-testid="stSidebar"] { background-color: #F1F5F9 !important; }
    section[data-testid="stSidebar"] * { color: #000000 !important; }
    .stButton>button {
        background-color: #1E40AF !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border-radius: 8px;
    }
    .stButton>button p { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU SÁCH (Anh cứ tiếp tục dán nội dung vào đây nhé)
DATA_BOOK = {
    "Lời nói đầu": """
    Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ. Và có những người thầy, mỗi ngày lặng lẽ đến trường, mang theo tri thức, tình thương và trách nhiệm để vun trồng tương lai cho đất nước.
Cuốn sách này kể về thầy Trần Trung Hậu – một giáo viên môn Tin học tại Trường THCS Thuận Hưng, Thành phố Cần Thơ. Hơn hai mươi sáu năm đứng lớp là hơn hai mươi sáu năm bền bỉ với bảng đen, phấn trắng, với những bài giảng đổi mới từng ngày, với niềm vui khi học trò tiến bộ và những trăn trở khi còn em nhỏ nào chưa theo kịp.
Đằng sau những danh hiệu cao quý như Nhà giáo Ưu tú, Huân chương Lao động hạng Ba, Bằng khen của Thủ tướng Chính phủ, Bằng khen Bộ Giáo dục và Đào tạo, hay hai lần đạt danh hiệu Chiến sĩ thi đua cấp thành phố, là một con người giản dị, khiêm nhường, sống trọn vẹn với nghề và với gia đình.
Đây không chỉ là câu chuyện về thành tích. Đây là câu chuyện về lòng yêu nghề, về sự bền bỉ, về trách nhiệm của một người thầy đã chọn cống hiến thay vì phô trương, chọn lặng thầm thay vì hào nhoáng, chọn gieo hạt thay vì chờ đợi vinh quang.
    """,
    
    "Chương 1: Tuổi thơ": """
1. Vùng đất Tân Lộc và những hạt giống đầu đời
Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ – cậu bé Trần Trung Hậu chào đời. Tuổi thơ của thầy gắn với hình ảnh quê hương bình dị: những con đường nhỏ, những hàng cây rợp bóng, tiếng gọi nhau thân tình của xóm làng và nếp sống chân chất của người miền Tây.
Chính mảnh đất ấy đã gieo vào lòng cậu bé những giá trị quan trọng nhất: sự siêng năng, lòng nhân hậu, tinh thần hiếu học và ý thức sống có ích cho cộng đồng.
2. Khát vọng học tập
Ngay từ nhỏ, Hậu đã yêu thích việc học. Không phải bằng những lời khoe khoang, mà bằng sự âm thầm cố gắng. Mỗi bài học mới là một cánh cửa mở ra thế giới rộng lớn hơn. Mỗi cuốn sách là một người thầy khác dẫn lối.
Khi công nghệ thông tin dần bước vào đời sống, cậu học trò ấy đặc biệt bị cuốn hút. Máy tính, phần mềm, những dòng lệnh… tất cả như mở ra một chân trời mới. Trong khi nhiều người còn xa lạ với công nghệ, Hậu nhìn thấy trong đó cơ hội thay đổi cách học, cách làm việc và cách con người kết nối với nhau.
3. Ước mơ trở thành người truyền lửa
Từ niềm yêu thích ấy, một ước mơ dần hình thành: trở thành người thầy. Không chỉ học cho mình, mà còn dạy lại cho người khác. Không chỉ giỏi chuyên môn, mà còn giúp học sinh tự tin bước vào tương lai.
Đó là ước mơ bình dị nhưng lớn lao – ước mơ của một người muốn sống có ích.
    """,
    
    "Chương 2: Bước chân vào nghề": """
1. Năm 2000 – Khởi đầu của một hành trình
Năm 2000, thầy Trần Trung Hậu chính thức bước vào nghề giáo. Một giáo viên trẻ mang theo nhiệt huyết, kiến thức và nhiều hoài bão đứng trước lớp học đầu tiên. Không ai trở thành người thầy lớn chỉ sau một ngày. Tất cả bắt đầu từ sự bỡ ngỡ, lo lắng và quyết tâm học hỏi không ngừng.
Ngày đầu đứng lớp, có lẽ thầy cũng như bao giáo viên trẻ khác: chuẩn bị bài thật kỹ, hồi hộp trước ánh mắt học sinh và tự nhủ phải làm tốt hơn mỗi ngày.
2. Khó khăn của người thầy dạy Tin học thời đầu
Dạy môn Tin học ở giai đoạn đầu không đơn giản. Cơ sở vật chất còn hạn chế, thiết bị chưa đồng bộ, điều kiện học tập của học sinh còn nhiều thiếu thốn. Nhưng khó khăn không làm thầy chùn bước.
Thay vì than phiền, thầy tìm cách thích nghi. Thay vì chờ điều kiện hoàn hảo, thầy tận dụng những gì đang có để mang đến bài học tốt nhất cho học sinh.
3. Trưởng thành qua từng lớp học
Mỗi năm học qua đi, thầy trưởng thành hơn trong nghề. Từ cách giảng bài, quản lý lớp, lắng nghe học sinh đến việc đổi mới phương pháp dạy học. Điều quý giá nhất nghề giáo mang lại không chỉ là kinh nghiệm, mà là khả năng hiểu con người.
Thầy hiểu rằng đằng sau mỗi học sinh là một hoàn cảnh khác nhau, một tính cách khác nhau và một cách tiếp nhận tri thức khác nhau.

    """,

    "Chương 3: Người thầy thời đại số": """
1. Không chỉ dạy máy tính
Nhiều người nghĩ dạy Tin học là dạy thao tác trên máy tính. Nhưng với thầy Trần Trung Hậu, Tin học là dạy tư duy logic, khả năng giải quyết vấn đề, tính sáng tạo và sự kiên nhẫn.
Một đoạn mã đúng không chỉ vì chạy được, mà còn vì người viết đã suy nghĩ rõ ràng. Một bài thực hành tốt không chỉ vì hoàn thành, mà vì học sinh hiểu mình đang làm gì.
2. Luôn học để không lạc hậu
Công nghệ thay đổi từng ngày. Người dạy Tin học nếu ngừng học sẽ nhanh chóng tụt lại phía sau. Vì thế, thầy luôn giữ cho mình tinh thần học tập suốt đời.
Sở thích cá nhân của thầy là nghiên cứu, học tập và trải nghiệm những vấn đề mới. Điều đó không chỉ là niềm vui riêng, mà còn trực tiếp làm giàu thêm những bài giảng trên lớp.
3. Truyền cảm hứng bằng sự cập nhật
Học sinh dễ nhận ra ai là người thật sự say mê kiến thức. Khi thấy thầy luôn tìm tòi cái mới, các em cũng học được tinh thần chủ động khám phá. Đó là bài học quý hơn cả kiến thức trong sách giáo khoa.

    """,

    "Chương 4: Những sáng kiến tâm huyết": """
1. Nâng cao chất lượng môn Tin học qua giáo dục kỹ năng sống
Một trong những sáng kiến nổi bật của thầy là Giải pháp nâng cao chất lượng môn Tin học cấp trung học cơ sở thông qua giáo dục kỹ năng sống.
Đây là tư duy tiến bộ: học Tin học không tách rời cuộc sống. Học sinh cần biết sử dụng công nghệ an toàn, hợp tác hiệu quả, giải quyết vấn đề, ứng xử văn minh trong môi trường số và có trách nhiệm với hành vi của mình.
Khi bài học gắn với đời sống, kiến thức trở nên có ý nghĩa hơn.
2. Ứng dụng Droicam và App Inventor 2
Thầy tiếp tục đổi mới với giải pháp ứng dụng phần mềm DroiCam và App Inventor 2 trên điện thoại thông minh nhằm nâng cao chất lượng môn Tin học lớp 6 tại Trường THCS Thuận Hưng.
Điều đáng quý ở sáng kiến này là sự gần gũi và thực tế. Thay vì coi điện thoại chỉ là thiết bị giải trí, thầy biến nó thành công cụ học tập. Học sinh được tiếp cận công nghệ bằng trải nghiệm trực tiếp, từ đó tăng hứng thú và khả năng sáng tạo.
3. Giá trị thật của sáng kiến
Sáng kiến không chỉ để báo cáo hay thi đua. Sáng kiến chân chính là điều giúp học sinh học tốt hơn, giúp giáo viên dạy hiệu quả hơn và giúp nhà trường phát triển hơn. Những gì thầy làm đều hướng về giá trị thực tế ấy.

    """,

    "Chương 5: Câu chuyện học trò": """
1. Một học trò rất giỏi nhưng kết quả thấp
Trong hành trình dạy học, có những niềm vui lớn, nhưng cũng có những nỗi buồn khiến người thầy day dứt rất lâu.
Thầy từng bồi dưỡng một học sinh có năng lực lập trình rất tốt. Em có kiến thức vững, tư duy nhanh, viết code tốt và đầy tự tin trước kỳ thi. Cả thầy lẫn trò đều hy vọng vào một kết quả xứng đáng.
Nhưng khi công bố điểm, em đạt số điểm rất thấp. Một kết quả khó lý giải. Cú sốc ấy làm học trò buồn bã, hụt hẫng. Với người thầy, đó cũng là nỗi đau thầm lặng.
2. Điều người thầy làm khi học trò thất bại
Trong khoảnh khắc ấy, điều quan trọng không còn là giải thưởng, mà là giữ cho học trò niềm tin vào chính mình.
Thầy không trách móc. Không tạo thêm áp lực. Thầy chọn cách an ủi, động viên và khích lệ em tiếp tục cố gắng. Thầy nói rằng giá trị của em không nằm ở một kỳ thi, và phía trước vẫn còn những sân chơi công bằng hơn để em thể hiện năng lực thật sự.
3. Trái ngọt của niềm tin
Sau đó, em tham gia kỳ thi Tin học trẻ. Và lần này, công sức được đền đáp xứng đáng: em đạt giải Nhất, đồng thời sản phẩm phần mềm của em cũng đạt giải Nhất.
Đó không chỉ là chiến thắng của học trò. Đó là chiến thắng của niềm tin, của sự đồng hành và của tình thương trong giáo dục.
Có những người thầy không chỉ dạy cách thành công, mà còn dạy cách đứng dậy sau thất bại.

    """,
    "Chương 6: CUỘC SỐNG ĐỜI THƯỜNG SAU BỤC GIẢNG": """
1. Người chồng, người cha trong gia đình
Sau giờ dạy, thầy trở về với mái ấm của mình – nơi có người vợ đồng hành và hai người con: một gái, một trai. Nếu ở trường thầy là người dẫn dắt học sinh, thì ở nhà thầy là chỗ dựa của gia đình.
Một người thành công ngoài xã hội nhưng thiếu trách nhiệm với gia đình thì thành công ấy chưa trọn vẹn. Thầy hiểu điều đó và luôn cố gắng cân bằng giữa công việc và tổ ấm.
2. Sự giản dị đáng quý
Nhiều người có thành tích lớn thường dễ tạo khoảng cách. Nhưng ở thầy Trần Trung Hậu, càng thành công càng khiêm nhường. Cuộc sống của thầy vẫn giản dị, chân thành và gần gũi.
Điều khiến người khác nể trọng không chỉ là danh hiệu, mà là cách sống sau danh hiệu.
3. Niềm vui từ việc học mỗi ngày
Có người thư giãn bằng nghỉ ngơi, có người bằng du lịch. Với thầy, niềm vui lớn là nghiên cứu và học cái mới. Tinh thần ấy giúp thầy luôn trẻ trong suy nghĩ, luôn tiến về phía trước và luôn có điều mới để chia sẻ với học trò.
    """,
    "Chương 7: NHỮNG DANH HIỆU VÀ GIÁ TRỊ THẬT": """
1. Nhà giáo Ưu tú – năm 2017
Danh hiệu Nhà giáo Ưu tú là sự ghi nhận cho cả một quá trình cống hiến. Nhưng để đi đến ngày được xướng tên là biết bao năm tận tâm, biết bao giờ lên lớp nghiêm túc và biết bao học sinh trưởng thành.
2. Huân chương Lao động hạng Ba – năm 2025
Huân chương Lao động hạng Ba là phần thưởng cao quý dành cho những đóng góp thiết thực và bền bỉ. Với thầy, đó không phải điểm kết thúc, mà là động lực để tiếp tục sống xứng đáng với niềm tin đã được trao gửi.
3. Những bằng khen và danh hiệu khác
Bằng khen của Thủ tướng Chính phủ, Bằng khen Bộ Giáo dục và Đào tạo, hai lần Chiến sĩ thi đua cấp thành phố… mỗi phần thưởng là một dấu mốc đẹp.
Nhưng có lẽ, phần thưởng lớn nhất vẫn là khi học trò cũ trở về, gọi một tiếng “thầy”, kể về cuộc sống ổn định và nói rằng những bài học năm xưa vẫn còn theo mình đến hôm nay.

""",  
    "Chương 8: TRIẾT LÝ SỐNG VÀ NGHỀ GIÁO": """
1. Dạy chữ đi cùng dạy người
Kiến thức có thể giúp một người kiếm sống. Nhân cách giúp họ sống đúng. Vì thế, dạy học không thể chỉ dừng ở sách vở.
2. Mỗi chuyến đò là một hành trình mới
Điều tâm đắc nhất của thầy về nghề giáo là cảm giác đã truyền thụ được kiến thức và bài học cuộc sống cho học sinh qua từng năm. Mỗi khóa học trò đi qua là một chuyến đò rời bến, mang theo hy vọng mới cho tương lai.
3. Truyền cảm hứng cho thế hệ trẻ
Thầy tin rằng một lời động viên đúng lúc có thể thay đổi cuộc đời một học sinh. Một tấm gương sống đẹp có thể tạo ra nhiều tấm gương khác. Và một người thầy tận tâm có thể âm thầm góp phần thay đổi xã hội.
""",   
    "Kết luận": """
    Giữa đời thường, có những con người sống lặng lẽ mà lớn lao. Thầy Trần Trung Hậu là một người như thế.
Từ cậu bé sinh ra nơi Tân Lộc đến người thầy được xã hội vinh danh; từ giáo viên trẻ năm 2000 đến nhà giáo với 26 năm đứng lớp; từ những bài giảng đầu tiên đến những sáng kiến đổi mới; từ những lo toan đời thường đến những thành tích cao quý – tất cả hợp thành chân dung đẹp của một nhà giáo chân chính.
Cuộc đời thầy nhắc chúng ta rằng: vĩ đại không nhất thiết phải là điều quá lớn lao. Đôi khi, vĩ đại là làm tốt công việc của mình suốt nhiều năm, sống tử tế với mọi người, không ngừng học hỏi và dành trái tim cho thế hệ mai sau.
Người thầy rồi sẽ già đi theo năm tháng. Nhưng những hạt giống tri thức và cảm hứng mà thầy gieo xuống sẽ tiếp tục nảy mầm trong biết bao cuộc đời khác.
Và đó mới là sự bất tử đẹp nhất của nghề giáo.
    """
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. GIAO DIỆN CHÍNH
st.markdown("<h1 style='text-align: center;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📖 MỤC LỤC")
selected = st.sidebar.radio("Chọn chương:", list(DATA_BOOK.keys()))

# Nội dung
st.markdown(f"<h2 style='color: #1E40AF !important;'>📌 {selected}</h2>", unsafe_allow_html=True)
content = DATA_BOOK[selected]
# Thêm style căn lề trực tiếp vào div để đảm bảo chắc chắn
st.markdown(f"<div class='noidung-sach' style='text-align: justify;'>{content}</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN
st.markdown("### 💬 Bạn đọc nhận xét")
with st.form("form_comment", clear_on_submit=True):
    name_user = st.text_input("Tên của anh/chị:")
    comment_user = st.text_area("Cảm nhận:")
    btn = st.form_submit_button("GỬI BÌNH LUẬN")
    if btn and name_user and comment_user:
        st.session_state.comments.insert(0, {
            "name": name_user,
            "text": comment_user,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

for c in st.session_state.comments:
    st.markdown(f"""
        <div style='background-color: #F3F4F6; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #1E40AF;'>
            <strong style='color: #1E40AF !important;'>👤 {c['name']}</strong> <small>({c['time']})</small><br>
            <p style='color: #000000 !important; margin-top: 5px; text-align: justify;'>{c['text']}</p>
        </div>
    """, unsafe_allow_html=True)
