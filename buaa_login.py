import sys
import requests as rq

USERNAME = "Student ID No."
PASSWORD = "Student ID PW"
USER_AGENT = "Opera/9.23 (Nintendo Wii; U; ; 1038-58; Wii Internet Channel/1.0; en)"
AUTH = rq.auth.HTTPBasicAuth(USERNAME, PASSWORD)
RETRY = 5


def light_off():
    pass


def light_on():
    pass


def check_network():
    try:
        res = rq.get("http://www.offer4u.cn/ping", timeout=3)
        res.close()
        if res.status_code == 204:
            return True
        return False

    except:
        return False


def logout():
    print("Logging out...")
    ua_dict = {'User-Agent': USER_AGENT}

    data = [
        ('action', 'logout'),
        ('username', USERNAME),
        ('password', PASSWORD),
        ('ajax', '1'),
    ]

    post = rq.post("https://gw.buaa.edu.cn/include/auth_action.php",
                   headers=ua_dict, data=data, verify=False)
    return post


def try_login():
    ua_dict = {'User-Agent': USER_AGENT}

    params = (
        ('ac_id', '22'),
        ('amp;url', 'https://gw.buaa.edu.cn:803/beihangview.php)'),
    )

    data = [
        ('action', 'login'),
        ('username', USERNAME),
        ('password', PASSWORD),
        ('ac_id', '22'),
        ('user_ip', ''),
        ('nas_ip', ''),
        ('user_mac', ''),
        ('save_me', '1'),
        ('ajax', '1'),
    ]

    post = rq.post('https://gw.buaa.edu.cn:803/beihanglogin.php',
                   headers=ua_dict, params=params, data=data, auth=AUTH, verify=False)
    return post


def login():
    for i in range(RETRY):
        print("Sending login request... attempt {}".format(i + 1))
        response = try_login().text[19:27]
        if response == "login_ok":
            print("Login Success.")
            break


def get_info():
    pass


def main():
    option = sys.argv[1]
    if option == "login":
        login()
    elif option == "logout":
        logout()
    else:
        print("Usage: \n login \n logout")


if __name__ == "__main__":
    main()
