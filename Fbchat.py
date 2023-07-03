import fbchat
from fbchat import Client, Message, ThreadType
import re
fbchat._state.FB_DTSG_REGEX = re.compile(r'"token":"(.*?)"')

username = 'aruncresta10@gmail.com'
password = 'fbchat@123'
client = Client(username, password)

thread_id = "100025222269196"  #for utsab
msg = "Dear students\nI cordially request to fill the above survey regarding the smart parking management system as BCT 3rd year students are selected in an idea pitching contest organised by the kathmandu metropolitan .\nRegards \nEr.Dinesh Gothe\nHead of Department\nKhwopa College of Engineering\n\nhttps://forms.office.com/pages/responsepage.aspx?id=ANUvPxRQGUupdAkOtgz_1UVmOI_bu4xHgKujCpL_4EBUQ1RCVVVIVUhSRElaOE40VzlSNE4wVFhYVi4u&fbclid=IwAR3Yf56hjhAmd4RuHYZr56ZTzA_nKhltQGDt8fckc8QzKDDvdZOV-SQVGoM\n"
client.send(Message(text=msg), thread_id=thread_id, thread_type=ThreadType.USER)
