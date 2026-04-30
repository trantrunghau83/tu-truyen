
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

    section[data-testid="stSidebar"] { background-color: #F1F5F9 !important; }
    section[data-testid="stSidebar"] * { color: #000000 !important; }
    
    /* Làm đẹp cho Selectbox chọn sách */
    div[data-baseweb="select"] > div {
        background-color: #1E40AF !important;
        color: white !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] * { color: white !important; font-weight: bold; }

    .stButton>button {
        background-color: #1E40AF !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border-radius: 8px;
    }
    .stButton>button p { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU ĐA TÁC PHẨM (THƯ VIỆN SỐ)
LIBRARY_DATA = {
    "Ký Ức Vùng Đất Tân Lộc": {
        "Lời mở đầu": """
        Tân Lộc là vùng đất của phù sa, của cây lành trái ngọt, của những con người chân chất và giàu nghĩa tình. Nơi đây không chỉ là quê hương của biết bao thế hệ, mà còn là miền ký ức sống động trong trái tim những người từng sinh ra, lớn lên và gắn bó với mảnh đất này.
<br><br>
        Cuốn sách “Ký ức vùng đất Tân Lộc” được viết với mong muốn lưu giữ những giá trị lịch sử, văn hóa, con người và hành trình phát triển của quê hương. Đây không chỉ là hồi ức về một vùng đất, mà còn là lời mời gọi tất cả cùng chung tay vun đắp để Tân Lộc ngày càng phát triển thịnh vượng hơn, đặc biệt trong lĩnh vực du lịch sinh thái và văn hóa cộng đồng.
        """,
        "Chương 1: Tân Lộc - Vùng đất bồi đắp bởi phù sa": """
        **1. Vị trí địa lý và dáng hình vùng đất**<br>
        Tân Lộc thuộc thành phố Cần Thơ, nằm giữa hệ thống sông ngòi chằng chịt của miền Tây Nam Bộ. Địa thế nơi đây được thiên nhiên ưu đãi với những doi đất màu mỡ, bao quanh bởi dòng nước hiền hòa.<br>
        Nhìn từ xa, Tân Lộc như một bức tranh xanh mướt, nơi những hàng cây nối tiếp nhau, những khu vườn sum suê trái ngọt và những mái nhà ẩn hiện dưới bóng cây.<br><br>
        **2. Những dòng sông nuôi lớn xóm làng**<br>
        Sông nước là mạch sống của Tân Lộc. Từ bao đời nay, con nước đã mang phù sa về bồi đắp đất đai, mang cá tôm về nuôi sống con người, và mang theo cả nhịp sống đặc trưng của miền quê sông nước. Trẻ em lớn lên cùng tiếng chèo xuồng, người lớn gắn bó với ghe thuyền, còn người già thường ngồi bên bến nước kể chuyện xưa.<br><br>
        **3. Đất đai màu mỡ và mùa trái ngọt**<br>
        Nhờ phù sa bồi tụ, Tân Lộc nổi tiếng với những khu vườn cây ăn trái trĩu quả: chôm chôm, mận, xoài, nhãn, sầu riêng... Mỗi mùa trái chín là một mùa vui, mùa của lao động và thành quả. Những khu vườn không chỉ mang lại kinh tế, mà còn tạo nên nét đẹp riêng cho quê hương.<br><br>
        **4. Thiên nhiên trong ký ức người dân**<br>
        Trong ký ức của người Tân Lộc, thiên nhiên không chỉ là cảnh vật mà là người bạn thân thiết. Đó là buổi sáng sương phủ mặt sông, trưa hè nghe tiếng chim gọi bầy, chiều xuống ngắm ánh hoàng hôn nhuộm đỏ dòng nước. Thiên nhiên ấy đã nuôi dưỡng tâm hồn bao thế hệ.
        """,
        "Chương 2: Dấu chân tiền nhân khai phá": """
        **Mở đầu chương**<br>

Mỗi vùng đất đều có một lịch sử riêng. Có nơi lịch sử được ghi bằng thành quách, bia đá. Có nơi lịch sử nằm trong những câu chuyện truyền đời, trong tên đất, tên sông, trong nếp sống của người dân và trong từng tấc đất được khai phá bằng mồ hôi của cha ông. Tân Lộc là một vùng đất như thế. <br><br>

Nơi đây không chỉ được bồi đắp bởi phù sa của sông Hậu, mà còn được bồi đắp bởi ý chí mở cõi, tinh thần kiên cường và dấu chân của bao lớp người đi trước. Trong dòng chảy ấy, dân gian còn lưu truyền những câu chuyện gắn với thời kỳ biến động của đất nước, khi bước chân của Nguyễn Ánh từng xuôi ngược miền Tây Nam Bộ trên hành trình dựng lại cơ đồ. Những giai thoại ấy, dù được kể bằng ký ức dân gian, vẫn làm cho vùng đất này thêm chiều sâu lịch sử và niềm tự hào. <br><br>

**1. Những lớp cư dân đầu tiên**<br>
	Thuở ban đầu, vùng đất Tân Lộc còn hoang sơ, cây cối um tùm, sông rạch chằng chịt, thú hoang nhiều hơn dấu chân người. Nhưng chính nơi tưởng như xa xôi ấy lại mở ra cơ hội sống cho những đoàn người đi tìm đất mới. <br><br>

Từ nhiều miền quê khác nhau, những lưu dân đã theo ghe thuyền xuôi dòng sông lớn đến đây. Họ mang theo gia đình, vài nông cụ đơn sơ, chút hạt giống và niềm hy vọng về một nơi an cư lạc nghiệp. Không có gì ngoài đôi bàn tay và ý chí, họ bắt đầu dựng chòi, khai hoang, đào mương, trồng lúa, trồng cây trái. <br><br>

Chính những con người vô danh ấy là những viên gạch đầu tiên dựng nên hình hài của Tân Lộc hôm nay. <br><br>       
        **2. Hành trình mở đất gian nan**<br>
        Khai phá miền đất mới chưa bao giờ là chuyện dễ dàng. Người xưa phải đối mặt với nước ngập theo mùa, muỗi mòng, bệnh tật, thú dữ và sự khắc nghiệt của thiên nhiên. Có những đêm mưa lớn nước dâng ngập mái lá. Có những mùa thất bát, cả nhà phải chắt chiu từng hạt gạo. <br><br>
Nhưng càng gian khó, ý chí con người càng sáng rõ. Họ học cách sống cùng con nước, tận dụng phù sa, cải tạo đất đai, chọn cây trồng phù hợp, dựng xóm làng theo nhịp điệu thiên nhiên. <br><br>
Từ vùng đất hoang vu, từng thửa ruộng được mở ra.
Từ bãi bồi hoang lạnh, từng khu vườn bắt đầu bén rễ.
Từ những mái lá tạm bợ, tiếng trẻ thơ đã cất lên giữa xóm làng.
Tân Lộc ra đời từ sự bền gan như thế.<br><br>
**3. Dấu xưa thời Nguyễn Ánh – Âm vang một thời mở nước**<br>

Trong ký ức dân gian vùng sông Hậu, nhiều nơi còn lưu truyền chuyện Nguyễn Ánh (sau này là vua Gia Long) từng đi qua miền Tây Nam Bộ trong những năm bôn tẩu, lánh nạn và tập hợp lực lượng vào cuối thế kỷ XVIII. Trên hành trình xuôi ngược giữa các nhánh sông lớn, vùng đất cù lao trù phú như Tân Lộc được xem là nơi ghe thuyền có thể dừng chân, tiếp nước, ẩn náu hoặc kết nối với cư dân địa phương. <br><br>

Dù không phải mọi chi tiết đều được ghi chép đầy đủ trong sử liệu địa phương, nhưng việc gắn vùng đất này với hành trình của Nguyễn Ánh cho thấy một điều quan trọng: Tân Lộc nằm trong không gian lịch sử lớn của Nam Bộ thời mở cõi và biến động quốc gia. <br><br>

Hãy hình dung vào một buổi sớm xa xưa, màn sương còn phủ trên mặt sông Hậu. Những chiếc thuyền lặng lẽ lướt qua cù lao. Người dân ven sông nhìn theo đoàn ghe mang theo vận mệnh của một thời đại. Có thể nơi đây từng chứng kiến bước chân của những con người làm nên lịch sử, từng nghe tiếng mái chèo gấp gáp giữa thời loạn lạc. <br><br>

Dù là giai thoại hay sự kiện được lưu truyền, điều còn lại đến hôm nay chính là niềm tự hào: vùng đất Tân Lộc không đứng ngoài lịch sử dân tộc. Tân Lộc đã hiện diện trong những năm tháng hào hùng của phương Nam. <br><br>

Lịch sử đôi khi không chỉ nằm trong sách vở.
Lịch sử còn sống trong lòng dân. <br><br>
        
**4. Lập làng, dựng xóm, giữ đất quê hương**<br>
        Khi cuộc sống dần ổn định, cư dân bắt đầu tổ chức cộng đồng bền vững hơn. Những xóm nhỏ hình thành ven sông, ven rạch. Người dân cùng nhau mở lối đi, dựng chợ, lập nơi sinh hoạt tín ngưỡng, chăm lo chuyện học hành cho con trẻ. <br><br>

Từ đó, Tân Lộc không còn là nơi “đến ở”, mà trở thành quê hương thật sự. Nơi có mồ mả tổ tiên, có ký ức gia đình, có tiếng gọi thân quen của xóm giềng. <br><br>

Bao thế hệ tiếp nối nhau giữ đất bằng lao động, bằng tình đoàn kết và bằng lòng gắn bó sâu nặng với nơi chôn nhau cắt rốn. <br><br>
        **5. Truyền thống cần cù qua bao thế hệ**<br>
        Di sản lớn nhất mà tiền nhân để lại cho Tân Lộc không chỉ là đất đai màu mỡ, mà là phẩm chất con người. Đó là sự cần cù, nhẫn nại, biết vượt khó và không ngại bắt đầu từ gian nan. <br><br>

Tinh thần ấy truyền từ ông bà đến cha mẹ, từ cha mẹ đến con cháu. Hôm nay, trong thời đại mới, truyền thống khai phá ấy không còn là phát rừng mở đất, mà là mở mang tri thức, đổi mới tư duy, phát triển kinh tế xanh và xây dựng quê hương giàu đẹp hơn. <br><br>

Cha ông mở đất bằng cuốc xẻng.
Con cháu hôm nay mở tương lai bằng tri thức và khát vọng.
        """,
        "Chương 3: Nếp sống và văn hóa Tân Lộc": """
        **1. Tình làng nghĩa xóm**<br>
        Ở Tân Lộc, hàng xóm không chỉ là người ở gần nhau, mà còn là người thân trong những lúc khó khăn. Khi nhà ai có việc, cả xóm cùng đến giúp.<br><br>
        **2. Chợ quê, đình làng và lễ hội**<br>
        Chợ quê là nơi trao đổi hàng hóa và gặp gỡ tình thân. Đình làng là nơi giữ gìn tín ngưỡng, tổ chức lễ hội, nhắc nhớ cội nguồn.<br><br>
        **3. Tiếng nói, giọng hò, câu hát**<br>
        Những câu hò, điệu lý, tiếng ru con vang lên giữa xóm làng là âm thanh đặc trưng của quê hương. Đó là nét văn hóa bình dị mà sâu sắc.<br><br>
        **4. Phong tục tập quán xưa và nay**<br>
        Từ cưới hỏi, giỗ chạp đến Tết Nguyên đán, người Tân Lộc luôn coi trọng lễ nghĩa, sự sum vầy và lòng biết ơn tổ tiên.
        """,
        "Chương 4: Những năm tháng chiến tranh và ký ức hào hùng": """
        **1. Tân Lộc trong thời loạn lạc**<br>
        Chiến tranh đã để lại nhiều đau thương cho quê hương. Những ngày bom đạn, cuộc sống người dân vô cùng gian khổ.<br><br>
        **2. Người dân và tinh thần yêu nước**<br>
        Dù khó khăn, người dân Tân Lộc vẫn một lòng yêu nước, góp sức người sức của cho kháng chiến.<br><br>
        **3. Những hy sinh thầm lặng**<br>
        Có những người mẹ tiễn con ra trận, có những người cha âm thầm gánh vác gia đình, có những thanh niên mãi mãi không trở về.<br><br>
        **4. Ký ức không thể nào quên**<br>
        Những mất mát ấy trở thành ký ức thiêng liêng, nhắc nhở thế hệ hôm nay biết quý trọng hòa bình.
        """,
        "Chương 5: Tân Lộc đổi mới và phát triển": """
        **Mở đầu chương**<br>

Có những vùng đất chỉ cần nhắc tên là người ta nhớ đến quá khứ. Nhưng cũng có những vùng đất vừa giữ được ký ức xưa, vừa bước mạnh vào tương lai bằng khát vọng mới. Tân Lộc chính là nơi như thế. <br><br>
Từ một cù lao yên bình giữa dòng sông Hậu, nơi từng gắn với ghe xuồng, bến nước, vườn cây và những con đường quê lặng lẽ… hôm nay Tân Lộc đang chuyển mình từng ngày. Sự đổi thay ấy không ồn ào, không vội vã, mà bền bỉ như chính tính cách của người dân nơi đây: chắc chắn, chân thành và giàu ý chí. <br><br>
Nếu ngày xưa cha ông mở đất bằng đôi tay chai sần, thì hôm nay con cháu đang mở tương lai bằng tri thức, bằng tư duy kinh tế mới và bằng niềm tin vào sức bật của quê hương. <br><br>
        **1. Con đường mới mở ra tương lai**<br>
        Ngày trước, hành trình đến Tân Lộc gắn liền với những chuyến đò ngang, những đoạn đường nhỏ quanh co và sự cách trở của sông nước. Mỗi chuyến đi là một lần chờ nước lớn, chờ con đò cập bến. Chính địa thế cù lao vừa là nét đẹp riêng, vừa là giới hạn của phát triển. <br><br>
Nhưng thời gian đã thay đổi tất cả. Những năm gần đây, hạ tầng giao thông tại khu vực Tân Lộc và vùng lân cận được quan tâm đầu tư mạnh hơn. Các tuyến đường nội ô được nâng cấp, mở rộng; giao thông kết nối với trung tâm khu vực Thốt Nốt và các địa bàn lân cận ngày càng thuận tiện hơn. Việc hoàn thiện hệ thống giao thông đã tạo điều kiện cho vận chuyển nông sản, phát triển dịch vụ và thu hút khách du lịch. <br><br>
Con đường mới không chỉ là mặt đường bê tông hay nhựa phẳng lì. Đó còn là con đường mở lối cho tư duy mới: từ sản xuất nhỏ lẻ sang liên kết giá trị; từ làm nông đơn thuần sang kinh tế trải nghiệm; từ vùng quê khép kín sang điểm đến mở cửa đón bạn bè bốn phương. <br><br>
Mỗi cây cầu được nối nhịp là một niềm vui. 
Mỗi tuyến đường hoàn thành là một hy vọng. 
Mỗi chuyến xe vào cù lao là một bước tiến của ngày mai. <br><br>
        **2. Kinh tế vườn – Từ mùa trái ngọt đến giá trị bền vững **<br>
        
Tân Lộc từ lâu được xem là vùng đất của cây lành trái ngọt. Nhờ lớp phù sa màu mỡ của sông Hậu, nơi đây phát triển mạnh các mô hình vườn cây ăn trái tập trung, trở thành lợi thế kinh tế đặc sắc của địa phương. Các loại trái cây theo mùa như mận, ổi, nhãn, xoài, chôm chôm… không chỉ là nông sản mà còn là “thương hiệu cảm xúc” của vùng đất này. <br><br>
Tuy nhiên, giá trị của Tân Lộc hôm nay không dừng ở chuyện bán trái cây. Người dân đã dần chuyển từ tư duy “bán sản phẩm” sang “bán trải nghiệm”. Du khách đến vườn không chỉ mua vài ký trái cây mang về, mà còn muốn tự tay hái quả, nghe kể chuyện làm vườn, ăn bữa cơm quê, chèo xuồng dưới rặng dừa, cảm nhận cuộc sống miệt vườn chân thật. <br><br>
Đó là bước chuyển quan trọng của kinh tế nông nghiệp hiện đại:
•	Tăng giá trị trên cùng diện tích đất. 
•	Giữ gìn cảnh quan sinh thái. 
•	Tạo thêm việc làm tại chỗ. 
•	Giữ người trẻ ở lại quê hương lập nghiệp. 
•	Kết nối nông dân với thị trường du lịch và dịch vụ. 
Một trái ổi có thể chỉ là nông sản.
Nhưng khi gắn với câu chuyện quê hương, nó trở thành giá trị văn hóa.
Một vườn cây có thể chỉ là nơi sản xuất.
Nhưng khi mở cửa đón du khách, nó trở thành tài sản du lịch.
<br><br>
        **3. Du lịch sinh thái – Đánh thức viên ngọc giữa sông Hậu**<br>
Theo các định hướng phát triển du lịch của thành phố Cần Thơ, cù lao Tân Lộc được xác định là không gian du lịch đặc thù giữa sông Hậu, có lợi thế lớn về sinh thái nông nghiệp, văn hóa sông nước và đời sống cộng đồng nguyên bản. Đây là nền tảng quan trọng để xây dựng sản phẩm du lịch khác biệt, tránh trùng lặp với các điểm đến khác. <br><br>
Tân Lộc có những điều mà nhiều nơi mơ ước:
Thiên nhiên còn nguyên nét hiền hòa
Không khí trong lành, cây xanh phủ mát, nhịp sống chậm rãi và không gian sông nước bao quanh tạo cảm giác thư thái hiếm có.
Bản sắc địa phương rõ nét
Từ tiếng nói, món ăn, cách tiếp khách đến nếp sinh hoạt hằng ngày – tất cả đều mang vẻ đẹp mộc mạc mà cuốn hút. <br><br>
Tài nguyên trải nghiệm đa dạng
•	Tham quan vườn trái cây 
•	Chèo xuồng trong rạch nhỏ 
•	Trải nghiệm làm nông dân 
•	Ẩm thực miệt vườn 
•	Tham quan nhà cổ 
•	Nghỉ homestay cộng đồng 
•	Ngắm bình minh và hoàng hôn trên sông Hậu 
Tiềm năng đầu tư còn rộng mở
Các mô hình nghỉ dưỡng sinh thái, farmstay, du lịch cộng đồng, sản phẩm OCOP, tour giáo dục trải nghiệm… đều có thể phát triển nếu được quy hoạch đồng bộ và đầu tư bài bản. <br><br>
Tân Lộc không cần trở thành nơi ồn ào náo nhiệt.
Tân Lộc chỉ cần là chính mình – xanh hơn, đẹp hơn, chuyên nghiệp hơn.
Bởi trong thời đại con người mệt mỏi vì tốc độ, những nơi bình yên như Tân Lộc lại càng quý giá. <br><br>
        **4. Diện mạo đô thị hôm nay – Sáng hơn, đẹp hơn, đáng sống hơn **<br>
        Sự phát triển của Tân Lộc không chỉ nằm ở du lịch hay nông nghiệp, mà còn thể hiện trong diện mạo dân cư và chất lượng sống. Những ngôi nhà mới khang trang mọc lên bên các tuyến đường sạch đẹp. Trường học, thiết chế văn hóa, cơ sở dân sinh từng bước được nâng cao. Đời sống vật chất của người dân ngày càng cải thiện rõ rệt. <br><br>
Điều đáng quý là giữa sự đổi thay ấy, Tân Lộc vẫn giữ được hồn quê. Vẫn còn đó hàng cây ven đường, tiếng chim gọi sáng, bữa cơm chan chứa nghĩa tình, nụ cười hiền hậu của người dân quê. <br><br>
Đó mới là phát triển bền vững:
Không đánh đổi bản sắc để lấy hiện đại.
Không đánh mất ký ức để chạy theo hào nhoáng.
Một đô thị đáng sống không chỉ có nhà cao đường rộng, mà còn là nơi con người thấy bình yên khi trở về.
        **5. Những việc cần làm để Tân Lộc bứt phá mạnh mẽ hơn **<br>
        Để đi xa hơn trong giai đoạn mới, Tân Lộc cần tiếp tục tập trung vào những hướng đi chiến lược:
Hoàn thiện hạ tầng kết nối
Giao thông, bến bãi, bãi đỗ xe, hệ thống chỉ dẫn du lịch, hạ tầng số.
Xây dựng thương hiệu điểm đến.
Tân Lộc cần được nhận diện rõ ràng trên bản đồ du lịch vùng Đồng bằng sông Cửu Long.
Đào tạo nguồn nhân lực địa phương. 
Người dân làm du lịch cần được hỗ trợ về kỹ năng đón khách, truyền thông, quản trị dịch vụ.
Phát triển sản phẩm đặc trưng. 
Ẩm thực địa phương, quà tặng nông sản chế biến, tour trải nghiệm văn hóa – giáo dục.
Thu hút đầu tư có chọn lọc. 
Ưu tiên các dự án xanh, thân thiện môi trường, tôn trọng cộng đồng địa phương.
<br><br>
**6.Niềm tin vào ngày mai**<br>
Không có vùng đất nào giàu lên chỉ nhờ thiên nhiên ưu đãi. Sự thịnh vượng chỉ đến khi con người biết nhìn ra giá trị của nơi mình đang sống và cùng nhau hành động. <br><br>
Tân Lộc đang có đất lành.
Đang có người tâm huyết.
Đang có cơ hội lớn.
Đang có tương lai mở rộng phía trước. 
Rồi sẽ đến ngày, khi nhắc đến Tân Lộc, người ta không chỉ nhớ một cù lao giữa sông Hậu, mà còn nhớ đến một hình mẫu phát triển xanh, đẹp, nhân văn và giàu bản sắc của Cần Thơ. <br><br>
Và khi ấy, những người con của quê hương sẽ mỉm cười tự hào rằng:
Chúng tôi đã không để vùng đất này ngủ quên trong ký ức.
Chúng tôi đã cùng nhau đánh thức tương lai của Tân Lộc.
""",
        "Chương 6: Người Tân Lộc và những câu chuyện đời thường": """
        **1. Những con người bình dị phi thường**<br>
        Đó là người nông dân cần mẫn, người thầy tận tụy, người mẹ hy sinh, người trẻ dám mơ ước và lập nghiệp.<br><br>
        **2. Ký ức tuổi thơ bên bến nước**<br>
        Tuổi thơ ở Tân Lộc gắn với tắm sông, bắt cá, hái trái, chạy chân trần trên con đường quê và những buổi trưa nghe tiếng ve kêu.<br><br>
        **3. Chuyện học hành, lập nghiệp xa quê**<br>
        Nhiều người con Tân Lộc đi xa để học tập, làm việc, nhưng trong tim luôn mang theo hình bóng quê nhà.<br><br>
        **4. Nỗi nhớ quê trong lòng người xa xứ**<br>
        Dù ở nơi đâu, chỉ cần nghe giọng nói miền Tây hay nhìn thấy dòng sông là nỗi nhớ quê lại ùa về.
        """,
        "Chương 7: Giữ gìn hồn quê cho thế hệ mai sau": """
        **1. Giá trị truyền thống cần được lưu giữ**<br>
        Những phong tục đẹp, tình làng nghĩa xóm, đạo lý uống nước nhớ nguồn cần được gìn giữ như báu vật tinh thần.<br><br>
        **2. Giáo dục tình yêu quê hương**<br>
        Thế hệ trẻ cần được học về lịch sử quê hương, hiểu công lao cha ông và tự hào về nơi mình sinh ra.<br><br>
        **3. Kết nối cộng đồng hôm nay**<br>
        Người dân địa phương, người xa quê, doanh nghiệp và chính quyền cần cùng nhau kết nối để xây dựng quê hương.<br><br>
        **4. Viết tiếp câu chuyện Tân Lộc**<br>
        Mỗi thế hệ sẽ viết thêm một chương mới cho Tân Lộc bằng hành động thiết thực, bằng lao động và khát vọng phát triển.
        """,
        "Kết luận": """
        **Tân Lộc – vùng đất của nghĩa tình**<br>
        Tân Lộc đẹp không chỉ bởi cây trái sum suê hay dòng sông hiền hòa, mà đẹp bởi con người sống chan hòa, thủy chung và nghĩa tình.<br><br>
        **Khi ký ức còn sống, quê hương còn mãi**<br>
        Một vùng đất sẽ trường tồn khi ký ức về nó vẫn còn được kể lại, được gìn giữ và tiếp nối. Ký ức vùng đất Tân Lộc không chỉ là câu chuyện của hôm qua, mà còn là niềm tin cho ngày mai – khi mọi người cùng chung tay xây dựng quê hương ngày càng thịnh vượng, văn minh và đáng tự hào.
        """
    },
    "Người Thầy Giữa Đời Thường": {
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
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. GIAO DIỆN CHÍNH
st.markdown("<h1 style='text-align: center; color: #1E40AF !important;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)

# Sidebar - CHỌN SÁCH VÀ CHỌN CHƯƠNG
st.sidebar.markdown("## 📖 CHỌN TÁC PHẨM")
selected_book = st.sidebar.selectbox("", list(LIBRARY_DATA.keys()))

st.sidebar.markdown("## 📑 MỤC LỤC")
selected_chapter = st.sidebar.radio("", list(LIBRARY_DATA[selected_book].keys()))

# Nội dung ở cột phải
st.markdown(f"<h3 style='text-align: center; color: #4B5563 !important;'>Tác phẩm: {selected_book}</h3>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color: #1E40AF !important;'>📌 {selected_chapter}</h2>", unsafe_allow_html=True)

content = LIBRARY_DATA[selected_book][selected_chapter]
st.markdown(f"<div class='noidung-sach'>{content}</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN
st.markdown("### 💬 Bạn đọc nhận xét")
with st.form("form_comment", clear_on_submit=True):
    name_user = st.text_input("Tên của anh/chị:")
    comment_user = st.text_area("Cảm nhận:")
    btn = st.form_submit_button("GỬI BÌNH LUẬN")
    if btn and name_user and comment_user:
        # Cập nhật bình luận kèm theo tên sách để biết độc giả đang bình luận cho sách nào
        st.session_state.comments.insert(0, {
            "name": name_user,
            "text": comment_user,
            "book": selected_book,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

# Chỉ hiển thị bình luận của cuốn sách đang được chọn
for c in st.session_state.comments:
    if c.get("book") == selected_book or "book" not in c:
        st.markdown(f"""
            <div style='background-color: #F3F4F6; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #1E40AF;'>
                <strong style='color: #1E40AF !important;'>👤 {c['name']}</strong> <small>({c['time']})</small><br>
                <p style='color: #000000 !important; margin-top: 5px; text-align: justify;'>{c['text']}</p>
            </div>
        """, unsafe_allow_html=True)
