class Locators(object):

    get_started_button = "//a[contains(text(),'Get started')]"
    Signup_name = "//body/div[@id='__next']/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]"
    Signup_email = "//body/div[@id='__next']/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/input[1]"
    Signup_country = "//div[contains(text(),'Country')]"
    password1 = "//div[1]/input"
    password2 = "//div[3]/input"
    start_my_podcast = "//button[contains(text(),'Start my podcast')]"

    # Sign in Locators
    login = "//a[contains(text(),'Login')]"
    login_email = "//div[1]/input[1]"
    login_password = "//div[3]/input[1]"
    login_button = "//button[contains(text(),'Login')]"

    # Create Podcast Locators
    CreatePodcast = "//a[@href='/account/podcasts/create']//p[1]"
    podcast_name = "//div[1]/input[1]"
    podcast_description = "//div[3]/textarea[1]"
    uploader = "//div[5]/div[1]/div[1]/input[1]"
    category = "//div[contains(text(),'Category')]"
    category_text = "#react-select-categorySelect-input"
    language = "//div[contains(text(),'Language')]"
    language_text = "#react-select-languageSelect-input"
    price = "//form[1]/div[11]/input[1]"
    welcome_message = "//form[1]/div[13]/textarea[1]"
    button_color = "//form[1]/div[17]/div[2]/input[1]"
    text_color = "//form[1]/div[18]/div[2]/input[1]"
    website = "//form[1]/div[19]/input[1]"
    instagram = "//form[1]/div[21]/input[1]"
    twitter = "//form[1]/div[23]/input[1]"
    facebook = "//form[1]/div[25]/input[1]"
    save = "//button[contains(@class,'btn-right btn')]"

    # edit podcast locators
    max_char_podcast = "//p[contains(text(),'Max Character Podcast')]"
    edit_podcast = "//span[contains(text(),'Edit')]"
    img_src = "//div[5]/div[1]/div[1]/img[1]"
    category_value = "//form[1]/div[7]/div[1]/div[1]/div[1]"
    language_value = "//form[1]/div[9]/div[1]/div[1]/div[1]/div[1]"
    podcast_price = "//form[1]/div[11]/input[1]"
    welcome_message_value = "//form[1]/div[13]/textarea[1]"
    podcast_slug_value = "//form[1]/div[15]/input[1]"
    rss_feed = "//input[@id='podcatcherLink']"
    button_color_value = "//form[1]/div[18]/div[2]/input[1]"
    text_color_value = "//form[1]/div[19]/div[2]/input[1]"
    website_value = "//form[1]/div[20]/input[1]"
    instagram_value = "//form[1]/div[22]/input[1]"
    twitter_value = "//form[1]/div[24]/input[1]"
    facebook_value = "//form[1]/div[26]/input[1]"

    # Validation Locators
    username_Validation = "//div[@class='invalid-feedback']"
    tost_validation = "//div[@class='Toastify__toast Toastify__toast--error']//div[1]"

    dev_podcast = "//a[@href='/account/podcasts/devpodcastmarch']"
    new_episode = "//a[@href='/account/podcasts/devpodcastmarch/episodes/create']"
    publish = "//button[text()='Publish']"
    episode_name = "episode_name"
    upload_audio = "//form/div[3]/div/div/input"
    episode_description = "//textarea[contains(@class,'form-control')]"
    episode_cover = "//form[1]/div[8]/div[1]/div[1]/input[1]"
    episode_typw = "//div[contains(text(),'Choose type of episode')]"
    episode_type_text = "//form[1]/div[12]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
    episode_email_message = "//form[1]/div[14]/textarea[1]"


