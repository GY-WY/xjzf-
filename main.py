import datetime
import requests
yplaceres = input('请输入预约场地(例如“西体育馆网球场地-1号场地”):')
ydate = input('请输入预约日期(例如“2025-05-15”):')
start_time = input('请输入开始时间(例如“22:00”):')
end_time = input('请输入结束时间(例如“23:30”):')
jd_url = 'http://gaut.xjzfu.edu.cn'
hesders = {
    'Host': 'gaut.xjzfu.edu.cn',
    'User-Agent':'Mozilla/5.0 (Linux; U; Android 14; zh-CN; 24069RA21C Build/UKQ1.240116.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 UWS/5.12.4.0 Mobile Safari/537.36 AliApp(DingTalk/7.5.36) com.alibaba.android.rimet/37747409 Channel/700159 language/zh-CN abi/64 xpn/xiaomi UT4Aplus/0.2.25 colorScheme/light',
    'Referer':'http://gaut.xjzfu.edu.cn/cdyyvue/changDiBaseindex/myChangDiApply',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie':'JSESSIONID=6B6949B9459248A877346AC5B5EE7DA8; gautappin=dingding; gautappid=fec5edfa306c45a4bc7cf066714c62ce; gautuserbindid=JSdNXP2EVM2jLKNeKxnpAQiEiE; gxqt_sso_sessionid=17794201657_5f7ad0065c1d47529fa93855ad106d38',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
date1 = {
    'frame_gxqt_user_id':'562540154623186926',
    'frame_gxqt_user_mobilephone':'18167406096',
    'frame_gxqt_user_username':'孙嘉禾',
    'frame_gxqt_user_xhorgh':'18167406096'
}
date2 = {
    'frame_gxqt_user_id':'0108520712031152347',
    'frame_gxqt_user_mobilephone':'17803106155',
    'frame_gxqt_user_username':'赵琰',
    'frame_gxqt_user_xhorgh':'17803106155'
}
date3 = {
    'frame_gxqt_user_id':'5942641650677352',
    'frame_gxqt_user_mobilephone':'15581517169',
    'frame_gxqt_user_username':'刘攀',
    'frame_gxqt_user_xhorgh':'15581517169'
}
datenull = {

}
date4 = {
    'frame_gxqt_user_id':'013600171466643552',
    'frame_gxqt_user_mobilephone':'17794201657',
    'frame_gxqt_user_username':'于亮',
    'frame_gxqt_user_xhorgh':'17794201657'
}
n_time = datetime.datetime.now()
time_str = n_time.strftime("%Y-%m-%d %H:%M:%S")
dateall = {
    'addtime':time_str,
    'approver':'(null)',
    'changDiBaseList':'(null)',
    'changDiCalendarList':'(null)',
    'deptid':'(null)',
    'edittime':'(null)',
    'id':'id=6c9198e5c85d4ad79d24f80e1a9d1ebc',
    'person_list':'',
    'person_num':'',
    'placeres_site_id':yplaceres,
    'real_duration':'1.5',
    'remark':'预约测试',
    'selectedPersonList':'(null)',
    'selectedTimes':'(null)',
    'unitid':'80bfc7c1ea134cbab17ea20d23418355',
    'use_date':ydate,
    'user_end_time':end_time,
    'user_start_time':start_time,
    'userid':'013600171466643552',
    'wfstatus':'2'
}
if __name__ == '__main__':
    response1 = requests.post(url=jd_url,headers=hesders,data=date1)
    response2 = requests.post(url=jd_url, headers=hesders, data=date2)
    response3 = requests.post(url=jd_url, headers=hesders, data=date3)
    responsenull = requests.post(url=jd_url, headers=hesders, data=datenull)
    response4 = requests.post(url=jd_url, headers=hesders, data=date4)
    responseall = requests.get(url=jd_url, headers=hesders)
    if '成功' in response1.text:
        print('孙嘉禾成功')
    else:
        print('孙嘉禾失败')
    #print(response1.text)

    if '成功' in response2.text:
        print('赵琰成功')
    else:
        print('赵琰失败')
    #print(response2.text)

    if '成功' in response3.text:
        print('刘攀成功')
    else:
        print('刘攀失败')
    #print(response3.text)

    if '成功' in responsenull.text:
        print('预约成功')
    else:
        print('预约失败')
    #print(responsenull.text)

    if '成功' in response4.text:
        print('于亮成功')
    else:
        print('于亮失败')
    #print(response4.text)
    if '成功' in responseall.text:
        print('GET成功')
    else:
        print('GET失败')
    #print(responseall.text)

