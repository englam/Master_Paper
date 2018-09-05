from datetime import datetime
import pandas as pd
import mysql.connector,multiprocessing, time


def save_to_mysql(_title,_brand,_model,_price,_wireless_type,_bug_title,_bug_content,_bug_author,_available_date,_bug_date,_feedbabck_author,_feedback_content):
    cnx = mysql.connector.connect(user='root',password='12345678', database='Amazon_Parse_Bugs')
    cursor = cnx.cursor()

    current_date = datetime.now()

    add_bug = ("INSERT INTO Products_Bugs "
                   "(title, brand, model_name, price, wireless_type,  bug_title, bug_content, bug_author,query_date,bug_date,available_date,feedback_author,feedback_content) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s)")


    data = (_title,_brand, _model, _price, _wireless_type,  _bug_title, _bug_content, _bug_author, current_date,_bug_date,_available_date,_feedbabck_author,_feedback_content)

    # Insert new employee
    cursor.execute(add_bug, data)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

title = 'NETGEAR Orbi Home WiFi System: AC3000 Tri Band Home Network with Router & Satellite Extender for up to 5,000sqft of WiFi coverage (RBK50) Works with Amazon Alexa'
wifi_type = '802.11bgn, 2.4 GHz Radio Frequency, 802.11 a/g/n/ac'
brand = 'NETGEAR'
model_name = 'RBK50-100NAS'
price = '$347.99'
avail_date = 'August 22, 2016'
bug_star = '3'
bug_title = 'starsGreat when it does not disconnect!'
bug_author = 'Mike B'
bug_time = 'on February 11, 2017'
bug_content = '''
Ok so here the nuts and bolts of it all! I have a 2100 square foot colonial home. I have an Asus 450 gb router that I have been using for over a year. This router was great because it rarely ever had to be reset and gave me consistent top speeds of 23 download Mbs (I pay for 20). Problem is that I have a lot of dead spots in my home. So after about a year with this router I couldnt handle not having all the dead spots. So I have started doing extensive research on the mesh router systems. I passed on the Eero because I wanted a tri-band router. I passed on the Velop because the limited ethernet ports. So I chose the Orbi. I new that the main issue of the Orbi was the firmware download. I knew that I had to perform the manual download so when I got the router I immediately connected just the router and downloaded the firmware automatically. Then I connected the Satellite and performed the manual download. It took about an hour to connect, and sync but that was me playing around with speed tests, and positioning too. Overall not too bad but when you pay this kind of money you expect immediate sync with automatic firmware updates to both units.

I also knew going into this purchase that the USB port is not active yet so that was not a big deal to me. Here are my priorities when i buy a router:
1- Coverage
2- Consistency
3- Speed

That should be the big three when someone pays this kind of money on something like this. Now I have a family of 5 and these are the devices we have:
3 - laptops
5 - smartphones
3 - FireTVs
3 - tablets
2 - Xboxes

So with 16 devices we need a beast of a unit. You get what you pay for right? Well let me tell you. Lets look at what happened next...

I went to all my rooms and was getting fantastic coverage. Even on the 2nd floor on the far end of the house. I was loving it, so I went outside about 50 feet to my back shed and wow I was getting 15 mb down (I pay for 20). Then I went near my satellite and what happened? I was getting 2 mps. I had to re-sync. Ok no big deal. After re-syncing my satellite I was getting 24 mps!! I was so happy at this point. Then I sat down after about an hour and was surfing the web and my web pages were taking a while to load. Quick speed test and only 2 mps down!! Had to reset my primary and then resync again! My wife knew of my irritation since we spent a lot of money on this and it is day 1. The rest of the evening was ok.
Today is day 2 and to make a long story short...I reset my system 4 times already. I dont need to call the tech line because I am not sitting on the phone for hours for them to guess at my problems. When I pay this kind of money I should be getting a lamborghini of a system not a yugo! So to sum it up...
1 - Coverage is a 5 out of 5 (when it works)
2 - Speed is a 4 out of 5
3 - Consistency is a ZERO. Now to be fair I am not sending this back today. I am going to give this about 2 weeks of solid usage. If these problems continue then it is going back and hello Velop. If I have no more problems, then I will come back to this review and revise it. Not happy at the moment. Better end this review now before my signal starts to dro....

UPDATE: Well i have given this more time, and since then I have contacted Netgear. I have worked with 3 technicians. The last one gave me some MAGIC beta firmware that did nothing for me. He advised me to return the product and then call him back. Well guess what i did. I returned the product and got another just to be fair. Connected it today and ran all the firmware updates. Speeds were 2 mb down!!! It is embarrassing! I cannot get this unit to work properly. By the way, I am a System Administrator so it is not like I am a noob. Played around with settings for about an hour and called the tech again. He is a level 2 so he is out until Monday. Looks like im screwed again. So after Monday this is going back too and getting the VELOP. I was more than fair with this product and lowered my review another star. I am still holding out hope for Monday when I speak with the tech again...

'''

feedback_author = 'Mike A'

feedback_content = '''
Ok so here the nuts and bolts of it all! I have a 2100 square foot colonial home. I have an Asus 450 gb router that I have been using for over a year. This router was great because it rarely ever had to be reset and gave me consistent top speeds of 23 download Mbs (I pay for 20). Problem is that I have a lot of dead spots in my home. So after about a year with this router I couldnt handle not having all the dead spots. So I have started doing extensive research on the mesh router systems. I passed on the Eero because I wanted a tri-band router. I passed on the Velop because the limited ethernet ports. So I chose the Orbi. I new that the main issue of the Orbi was the firmware download. I knew that I had to perform the manual download so when I got the router I immediately connected just the router and downloaded the firmware automatically. Then I connected the Satellite and performed the manual download. It took about an hour to connect, and sync but that was me playing around with speed tests, and positioning too. Overall not too bad but when you pay this kind of money you expect immediate sync with automatic firmware updates to both units.

I also knew going into this purchase that the USB port is not active yet so that was not a big deal to me. Here are my priorities when i buy a router:
1- Coverage
2- Consistency
3- Speed

That should be the big three when someone pays this kind of money on something like this. Now I have a family of 5 and these are the devices we have:
3 - laptops
5 - smartphones
3 - FireTVs
3 - tablets
2 - Xboxes

So with 16 devices we need a beast of a unit. You get what you pay for right? Well let me tell you. Lets look at what happened next...

I went to all my rooms and was getting fantastic coverage. Even on the 2nd floor on the far end of the house. I was loving it, so I went outside about 50 feet to my back shed and wow I was getting 15 mb down (I pay for 20). Then I went near my satellite and what happened? I was getting 2 mps. I had to re-sync. Ok no big deal. After re-syncing my satellite I was getting 24 mps!! I was so happy at this point. Then I sat down after about an hour and was surfing the web and my web pages were taking a while to load. Quick speed test and only 2 mps down!! Had to reset my primary and then resync again! My wife knew of my irritation since we spent a lot of money on this and it is day 1. The rest of the evening was ok.
Today is day 2 and to make a long story short...I reset my system 4 times already. I dont need to call the tech line because I am not sitting on the phone for hours for them to guess at my problems. When I pay this kind of money I should be getting a lamborghini of a system not a yugo! So to sum it up...
1 - Coverage is a 5 out of 5 (when it works)
2 - Speed is a 4 out of 5
3 - Consistency is a ZERO. Now to be fair I am not sending this back today. I am going to give this about 2 weeks of solid usage. If these problems continue then it is going back and hello Velop. If I have no more problems, then I will come back to this review and revise it. Not happy at the moment. Better end this review now before my signal starts to dro....

UPDATE: Well i have given this more time, and since then I have contacted Netgear. I have worked with 3 technicians. The last one gave me some MAGIC beta firmware that did nothing for me. He advised me to return the product and then call him back. Well guess what i did. I returned the product and got another just to be fair. Connected it today and ran all the firmware updates. Speeds were 2 mb down!!! It is embarrassing! I cannot get this unit to work properly. By the way, I am a System Administrator so it is not like I am a noob. Played around with settings for about an hour and called the tech again. He is a level 2 so he is out until Monday. Looks like im screwed again. So after Monday this is going back too and getting the VELOP. I was more than fair with this product and lowered my review another star. I am still holding out hope for Monday when I speak with the tech again...

'''


feedback_author2 = ""
feedback_content2 = None

avail_date = datetime.strptime(avail_date, "%B %d, %Y")

bug_time = bug_time.replace("on ","")
bug_time= datetime.strptime(bug_time, "%B %d, %Y")

#p = multiprocessing.Process(target=save_to_mysql, args=(title,brand,model_name,price,wifi_type,bug_title,bug_content,bug_author,avail_date,bug_time,feedback_author,feedback_content,))
#p2 = multiprocessing.Process(target=save_to_mysql, args=(title,brand,model_name,price,wifi_type,bug_title,bug_content,bug_author,avail_date,bug_time,feedback_author2,feedback_content2,))


for i in range (1,101):
    p = multiprocessing.Process(target=save_to_mysql, args=(title, brand, model_name, price, wifi_type, bug_title, bug_content, bug_author, avail_date, bug_time,feedback_author, feedback_content,))
    p2 = multiprocessing.Process(target=save_to_mysql, args=(title, brand, model_name, price, wifi_type, bug_title, bug_content, bug_author, avail_date, bug_time,feedback_author2, feedback_content2,))

    p.start()
    p2.start()
    print ("[*] Count:",i)

#save_to_mysql(title,brand,model_name,price,wifi_type,bug_title,bug_content,bug_author,avail_date,bug_time,feedback_author,feedback_content)


#save_to_mysql(title,brand,model_name,price,wifi_type,bug_title,bug_content,bug_author,avail_date,bug_time,feedback_author2,feedback_content2)

