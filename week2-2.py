def collect_user_data():
    name = input("請輸入您的姓名: ")
    age = int(input("請輸入您的年齡: "))
    height = float(input("請輸入您的身高（米）: "))
    favorite_color = input("請輸入您喜愛的顏色: ")
    return {
        "name": name,
        "age": age,
        "height": height,
        "favorite_color": favorite_color
    }

def format_user_data(user_data):
    return f"{user_data['name']}, {user_data['age']}歲, 身高{user_data['height']}米, 喜愛的顏色是{user_data['favorite_color']}。"

def main():
    user_data = collect_user_data()
    summary = format_user_data(user_data)
    print(summary)

if __name__ == "__main__":
    main()
