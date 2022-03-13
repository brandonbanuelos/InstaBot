from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os

class InstagramBot(object):
    def __init__(self, email, password,comments):
            self.email = email
            self.password = password
            self.browser = webdriver.Chrome(executable_path= os.getcwd() + os.path.sep + 'chromedriver')
            self.comments = comments
            
    def login(self):
            self.browser.get('https://www.instagram.com/?hl=en')
            time.sleep(4)
            emailInput = self.browser.find_element_by_name('username')
            passwordInput = self.browser.find_element_by_name('password')
            emailInput.send_keys(self.email)
            passwordInput.send_keys(self.password)
            loginButton = self.browser.find_element_by_class_name('L3NKy')
            loginButton.click()
            time.sleep(4)

    def searchHashtag(self, hashtag):
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag)
            time.sleep(5)

    def likePicture(self):
            time.sleep(2)
            likeButton = self.browser.find_element_by_class_name('fr66n')
            
            time.sleep(2)
            elem = self.browser.find_element_by_css_selector("span.fr66n > button > div > span > svg").get_attribute("aria-label")
            
            if elem == 'Unlike':
                print('Already liked this photo')
                return 0

            else:
                likeButton.click()
                print('Liked photo')
                return 1
           
    def commentOnPicture(self):
            commentChances = [0,1]
            willComment = random.choice(commentChances)

            if willComment > 0:
                
                try:
                    self.browser.find_element_by_class_name('Ypffh')
                    commentBox = self.browser.find_element_by_class_name('Ypffh')
                    commentBox.click()
                    commentBox = self.browser.find_element_by_class_name('Ypffh')
                    randomComment = random.choice(self.comments)
                    commentBox.send_keys(randomComment)
                    time.sleep(2)
                    
                    if "@" in randomComment:
                        commentBox.send_keys(Keys.ENTER)
                        commentBox.send_keys(Keys.ENTER)
                        
                    commentBox.send_keys(Keys.ENTER)
                    
                    time.sleep(1)
                    
                    retryComment = self.browser.find_element_by_class_name('yWX7d').text
                    
                    if retryComment == "Retry":
                        print("Couldn't comment due to Instagram")
                        return 0
                    else:
                        print("Commented: ", randomComment)
                        return 1
                
                except:
                    print("Couldn't comment. Comments turned off")
                    return 0

            else:
                print("Skipped comment for added secrecy")
                return 0
                

    def clickPicture(self):
            picture = self.browser.find_element_by_class_name('v1Nh3')
            picture.click()

    def scrollRight(self):
            scrollButton = self.browser.find_element_by_class_name('coreSpriteRightPaginationArrow')
            scrollButton.click()

    def followUser(self):
            followButton = self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            accountFollowed = self.browser.find_element_by_class_name('yWX7d').text
            
            if followButton.text == 'Following':
                print('Already following', accountFollowed)
                return 0

            else:
                followButton.click()
                accountFollowed = self.browser.find_element_by_class_name('yWX7d').text
                print('Followed: ', accountFollowed)
                return 1

    def doFollowLikeCommentScroll(self, amount, boolFollow, boolComment):
        index = 1
        self.clickPicture()

        print('Starting bot processes')

        accountsFollowed = 0
        postsLiked = 0
        commentsPosted = 0
        
        for index in range(amount):
            time.sleep(3)

            try:
                self.browser.find_element_by_class_name('yWX7d').text
                accountTargeted = self.browser.find_element_by_class_name('yWX7d').text
                
            except:
                print("Skipped no picture")
                self.scrollRight()
                
            print('\nPerson number: ', index+1)
            print('Targeted account: ', accountTargeted)
            time.sleep(4)

            if boolFollow == True:
                accountsFollowed += self.followUser()
                time.sleep(2)
                
            postsLiked += self.likePicture()
            time.sleep(2)
            
            if boolComment == True:
                commentsPosted += self.commentOnPicture()
                time.sleep(4)
                
            self.scrollRight()
            index+=1
            time.sleep(1)

        print('\nDone doing bot stuff')
        print('Liked ', postsLiked, ' photo(s)')
        print('Commented on ', commentsPosted, ' photo(s)')
        print('Followed ', accountsFollowed, ' account(s)')
        
exampleComments =['lets build','lets go',
                   'you wanna work?',
                   'i like this!',
                   'looking good!',
                   'keep up the hard work!',
                   'keep up the grind!',
                   'i enjoyed!',
                   'keep moving',
                   'i like what i see!',
                   'i just dropped a single maybe check it out? thanks!',
                   'nice! maybe you could check out some of my stuff too? thanks!',
                   'nice work and if you like chill music maybe id be of interest!']

bot = InstagramBot('youremail@gmail.com', 'yourpassword', exampleComments)

bot.login()              
time.sleep(3)
bot.searchHashtag('enterhashtaghere')
time.sleep(3)
bot.doFollowLikeCommentScroll(150,False, True)

#every 7th comment should be different
#supposedly Instagram only allows
#1000 likes/day
#400-500 comments a day
#250 follows
#250 unfollows
#lower with less or if account is newer
