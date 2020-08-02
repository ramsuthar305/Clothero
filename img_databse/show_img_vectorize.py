import pandas aspd
import os
t_img_url = ["https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/12029466/2020/7/29/059e98dd-604b-4dc0-9836-534d139248221596032265588AnoukWomenNavyBlueSolidStraightKurtaTshirtsAmericanCrewMenTs2.jpg",

             "https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/5508761/2018/4/30/11525068766496-HERENOW-Men-Teal-Printed-Round-Neck-T-shirt-2021525068766307-1.jpg",
             "https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/11548544/2020/3/9/5eeaead2-de8e-45fb-99d9-c5bccf21e7ea1583748694212-Huetrap-Men-Tshirts-6441583748692050-1.jpg",
             "https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/1964364/2017/6/23/11498197904638-HERENOW-Men-Navy-Blue-Solid-Henley-Neck-T-shirt-6741498197904414-1.jpg",
             "https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/1997302/2017/8/23/11503492424739-Roadster-Men-Red-Printed-Round-Neck-T-shirt-4971503492424397-1.jpg",
             "https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/11748120/2020/7/7/48d5564c-8166-4981-a50a-4414e59e49bc1594111528301ShangrilaCreationGold-TonedPinkSilkBlendWovenDesignPaithaniS1.jpg",

             "https://assets.ajio.com/medias/sys_master/root/h53/h74/15216776806430/-473Wx593H-461085141-blue-MODEL3.jpg",
             "https://assets.ajio.com/medias/sys_master/root/h22/hc3/16010300588062/-473Wx593H-461005997-multi-MODEL.jpg",
             "https://assets.ajio.com/medias/sys_master/root/ajio/catalog/5efa2b5af997dd433b463c86/-473Wx593H-461209675-navy-MODEL.jpg",
             "https://assets.ajio.com/medias/sys_master/root/ajio/catalog/5f0cab777cdb8c721b7bf2dd/-473Wx593H-460545545-green-MODEL3.jpg",
             "https://assets.ajio.com/medias/sys_master/root/h9f/hd0/16053450932254/-473Wx593H-461134695-yellow-MODEL4.jpg",
             ]
j_img_url = ["https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/10476518/2019/8/22/1ff738e2-aeb0-41e9-b81e-4046dc02d6221566465605679-LOCOMOTIVE-Men-Navy-Blue-Tapered-Fit-Jeans-8201566465604503-1.jpg",
             "https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/4451364/2019/11/25/8d57e2fc-4c1b-4f01-b129-40d3412eee5f1574687095197-Roadster-Fast-and-Furious-Men-Blue-Slim-Fit-Mid-Rise-Low-Dis-1.jpg",
             "https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/productimage/2020/7/7/9f7e7546-925e-4c07-b9de-1ec252b7cf7b1594100227721-1.jpg",
             "https://assets.ajio.com/medias/sys_master/root/hed/h2f/15258040795166/-473Wx593H-460398814-blue-MODEL4.jpg",
             "https://assets.ajio.com/medias/sys_master/root/h86/h9d/16764497756190/-473Wx593H-460596707-blue-MODEL6.jpg",
             "https://assets.ajio.com/medias/sys_master/root/h34/h27/14914075230238/-473Wx593H-460441264-grey-MODEL4.jpg",
             "https://assets.ajio.com/medias/sys_master/root/h86/h9d/16764497756190/-473Wx593H-460596707-blue-MODEL6.jpg",
             "https://assets.ajio.com/medias/sys_master/root/ajio/catalog/5f03a4d9f997dd433b497e99/-473Wx593H-461214287-blue-MODEL5.jpg", ]
os.makedirs("Data")
show_data = pd.DataFrame(columns=['Type', "BS4", "Vector"])
for i, val in enumerate(t_img_url):

    name = f"Data/Tshirt-{i}.jpg"
    urllib.request.urlretrieve(val, name)
    bs4 = convertBase64(name)
    vc = cls_obj.process(name)
    type_ = "Tshirt"

    show_data.append([type_, bs4, vc])
for i, val in enumerate(j_img_url):

    name = f"Data/Jeans-{i}.jpg"
    urllib.request.urlretrieve(val, name)
    bs4 = convertBase64(name)
    vc = cls_obj.process(name)
    type_ = "Jeans"
    row = (type_, bs4, vc)
    row = [type_, bs4, vc]
    show_data.append(row)
print(show_data.head())
show_data.to_csv("show.csv", index=0)
