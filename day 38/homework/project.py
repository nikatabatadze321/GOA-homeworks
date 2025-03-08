import time

users = {}

def register():
    print("რეგისტრაციისთვის გთხოვთ შეავსოთ მონაცემები.")
    username = input("გამოიყენეთ სახელი: ")
    if username in users:
        print("ამ სახელით უკვე დარეგისტრირებულა მომხმარებელი.")
        return
    password = input("შეიყვანეთ პაროლი: ")
    users[username] = {
        "password": password,
        "balance": 0,
        "name": username,
        "email": "",
        "phone": "",
    }
    print(f"{username} წარმატებით დარეგისტრირდა.")

def reset_password():
    username = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
    if username not in users:
        print("მომხმარებელი არ მოიძებნა.")
        return
    new_password = input("შეიყვანეთ ახალი პაროლი: ")
    users[username]["password"] = new_password
    print(f"პაროლი წარმატებით შეიცვალა!")

def login():
    username = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
    if username not in users:
        print("მომხმარებელი არ მოიძებნა.")
        return None
    password = input("გთხოვთ, შეიყვანოთ პაროლი: ")
    if users[username]["password"] == password:
        print(f"{username} წარმატებით შევიდა!")
        return username
    else:
        print("პაროლი არასწორია.")
        return None

def withdraw(username):
    amount = float(input("რაოდენობა, რომელიც გსურთ გამოტანოთ: "))
    if amount <= 0:
        print("გთხოვთ, შეიყვანოთ დადებითი თანხა.")
        return
    if users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        print(f"თქვენ წარმატებით გამოიტანეთ {amount} ლარი. თქვენი ახალი ბალანსია: {users[username]['balance']} ლარი.")
    else:
        print("მიუწვდომელია საკმარისი თანხა.")

def deposit(username):
    amount = float(input("რაოდენობა, რომელიც გსურთ შეიტანოთ: "))
    if amount <= 0:
        print("გთხოვთ, შეიყვანოთ დადებითი თანხა.")
        return
    users[username]["balance"] += amount
    print(f"თქვენ წარმატებით შეიტანეთ {amount} ლარი. თქვენი ახალი ბალანსია: {users[username]['balance']} ლარი.")

def buy_item(username):
    items = {
        "1": {"name": "კომპიუტერი", "price": 1000},
        "2": {"name": "მობილური ტელეფონი", "price": 500},
        "3": {"name": "პლაზმური ტელევიზორი","price":1500},
        "3": {"name": "ფლეი სთეიშენ 5","price":2000},
        "4": {"name": "ჭკვიანი საათი","price":500},
        "5": {"name": "სამსუნგ გალაქსის ჭკვიანი საათი","price":500},
        "6": {"name": "ვირტუალური რეალობის სათვალე","price":500},
        "7": {"name": "მაქბუქ პრო ","price":1500},
        "8": {"name": "აირპოდსები","price":300},
        "9": {"name": "ხმის ჩამხშობი ყურსასმენი ","price":500},
        "10": {"name": "GoPro კამერა","price":1500},
        "11": {"name": "უსარკო კამერა","price":1000},
        "12": {"name": "ნებისმიერი კამერის ლინზა ","price":350},
        "13": {"name": "DSLR ფოტოაპარატი ","price":1500},
        "14": {"name": "360 ვიდეო კამერა","price":1000},
        "15": {"name": "","price":1500},
        "16": {"name": "DJI დრონი","price":2000},
        "17": {"name": "ლეპტოპი(MSI Titan 18 HX)","price":5399},
        "18": {"name": "ლეპტოპი(MSI Raider GE68 HX 14VHG-612GE)","price":8999},
        "19": {"name": "ლეპტოპი(Acer Predator Helios Neo 16)","price":6064},
        "20": {"name": "ლეპტოპი(Acer Nitro 15)","price":4044},
        "21": {"name": "ლეპტოპი(MSI Cyborg 15 )","price":3799},
        "22": {"name": "ლეპტოპი(MSI Sword 16)","price":5390},
        "23": {"name": "ლეპტოპი(Asus ROG Strix 18)","price":5099},
        "24": {"name": "ლეპტიპი(Dell Alienware Gaming/210-BKWQ)","price":8399},
        "25": {"name": "ლეპტოპი(Asus ROG Flow X16)","price":5899},
        "26": {"name": "ლეპტოპი(Asus TUF 15)","price":4399},
        "27": {"name": "ლეპტოპი(Acer Predator Helios Neo 18)","price":6061},
        "28": {"name": "ლეპტოპი(Dell XPS 9530)","price":7699},
        "29": {"name": "ლეპტოპი(Acer PH3D15-71)","price":10799},
        "31": {"name": "ლეპტოპი(Acer Nitro 5)","price":4230},
        "32": {"name": "აიფონი(8)","price":700},
        "33": {"name": "აიფონი(8 pro)","price":900},
        "34": {"name": "აიფონი(x)","price":999},
        "35": {"name": "აიფონი(11)","price":699},
        "36": {"name": "აიფონი(11 pro)","price":999},
        "37": {"name": "აიფონი(11 pro max)","price":1200},
        "38": {"name": "აიფონი(12)","price":799},
        "39": {"name": "აიფონი(12 pro)","price":1099},
        "40": {"name": "აიფონი(12 pro max)","price":1499},
        "41": {"name": "აიფონი(13)","price":899},
        "42": {"name": "აიფონი(13 pro)","price":1199},
        "43": {"name": "აიფონი(13 pro max)","price":1699},
        "44": {"name": "აიფონი(14)","price":2000},
        "45": {"name": "აიფონი(14 pro)","price":2600},
        "46": {"name": "აიფონი(14 pro max)","price":3200},
        "47": {"name": "აიფონი(15)","price":2500},
        "48": {"name": "აიფონი(15 pro)","price":3000},
        "49": {"name": "აიფონი(15 pro max)","price":3500},
        "50": {"name": "აიფონი(16)","price":2800},
        "51": {"name": "აიფონი(16 pro)","price":3749},
        "52": {"name": "აიფონი(16 pro max)","price":5599},

        
        

        
    
    }
    
    print("გთხოვთ, აირჩიეთ ნივთი:")
    for key, item in items.items():
        print(f"{key}. {item['name']} - {item['price']} ლარი")
    
    choice = input("აირჩიეთ ნივთი (1 დან 52 ჩათვლით ): ")
    if choice not in items:
        print("არასწორი არჩევანი.")
        return
    item = items[choice]
    if users[username]["balance"] >= item["price"]:
        users[username]["balance"] -= item["price"]
        print(f"{item['name']} წარმატებით იყიდეთ. თქვენი ახალი ბალანსია: {users[username]['balance']} ლარი.")
    else:
        print("მიუწვდომელია საკმარისი თანხა.")

def change_username(username):
    new_username = input("გთხოვთ, შეიყვანოთ ახალი სახელი: ")
    if new_username in users:
        print("ამ სახელით უკვე არსებობს მომხმარებელი.")
    else:
        users[new_username] = users.pop(username)
        users[new_username]["name"] = new_username
        print(f"სახელი წარმატებით შეიცვალა!")

def count_users():
    print(f"რეგისტრირებული მომხმარებლების რაოდენობა: {len(users)}")

def main_menu():
    print("ბანკის მენიუ:")
    print("1. რეგისტრაცია")
    print("2. შესვლა")
    print("3. პაროლის აღდგენა")
    print("4. მომხმარებლის სახელი შეცვალე")
    print("5. მომხმარებლების რაოდენობა")
    print("6. გამოსვლა")
    
    choice = input("აირჩიეთ ოპცია: ")
    if choice == "1":
        register()
    elif choice == "2":
        username = login()
        if username:
            user_menu(username)
    elif choice == "3":
        reset_password()
    elif choice == "4":
        username = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
        if username in users:
            change_username(username)
        else:
            print("მომხმარებელი არ მოიძებნა.")
    elif choice == "5":
        count_users()
    elif choice == "6":
        print("გამოსვლა...")
        time.sleep(1)
        return
    else:
        print("არასწორი არჩევანი.")
        main_menu()

def user_menu(username):
    while True:
        print(f"\n{username} - თქვენი მენიუ:")
        print("1. ფულის გამოტანა")
        print("2. ფულის შეტანა")
        print("3. ნივთის ყიდვა")
        print("4. გამოსვლა")
        
        choice = input("აირჩიეთ ოპცია: ")
        if choice == "1":
            withdraw(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            buy_item(username)
        elif choice == "4":
            print("გამოსვლა...")
            time.sleep(1)
            break
        else:
            print("არასწორი არჩევანი.")

if __name__ == "__main__":
    while True:
        main_menu()