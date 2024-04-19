
import re
import string
import pandas as pd
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


def format_phone_number(phone_number):
    pattern = r'(\d{3})(\d{3})(\d{4})'
    formatted_number = re.sub(pattern, '\1-\2-\3', phone_number)
    return formatted_number


def validate_name(name):
    # 이름이 빈 문자열인지 확인
    if not name:
        return False
    # 이름의 길이가 8글자 이하인지 확인
    if len(name) <= 8:
        # 모든 문자가 알파벳 또는 공백인지 확인
        if all(char in string.ascii_letters or char in string.whitespace for char in name):
            return True
    return False


def validate_id(id):
    # ID가 빈 문자열인지 확인
    if not id:
        return False

    # ID가 최소 2글자 이상인지 확인
    if len(id) < 4:
        return False

    # ID가 최대 8글자 이하인지 확인
    if len(id) > 8:
        return False

    # ID가 영어와 숫자로만 이루어졌는지 확인
    pattern = r'^[a-zA-Z]{2,}[0-9]{1,}$'
    if re.match(pattern, id):
        return True
    else:
        return False


def validate_pwd(pwd):
    # 비밀번호가 빈 문자열인지 확인
    if not pwd:
        return False

    # 비밀번호가 8글자 이상인지 확인
    if len(pwd) < 8:
        return False

    # 비밀번호가 최대 20글자 이하인지 확인
    if len(pwd) > 20:
        return False

    # 비밀번호가 영어 대소문자, 숫자, 특수문자를 모두 포함하는지 확인
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$'
    if re.match(pattern, pwd):
        return True
    else:
        return False


def validate_user_input(email, name, user_id, password, phone_number):
    return (validate_email(email) and
            validate_name(name) and
            validate_id(user_id) and
            validate_pwd(password))


def add_user_info(df, email, name, user_id, password, phone_number):
    # 입력 값들을 검증
    if validate_email(email) and validate_name(name) and validate_id(user_id) and validate_pwd(password):
        # DataFrame에 추가
        df = pd.concat([df, pd.DataFrame({
            'email': [email],
            'name': [name],
            'id': [user_id],
            'password': [password],
            'phone_number': [phone_number]
        })], ignore_index=True)
        return df  # append 후에 반환
    else:
        print("유효하지 않은 정보가 있습니다.")
        return df  # 유효하지 않은 경우에도 반환

def append_to_csv(df, file_name):
    try:
        # 데이터프레임을 CSV 파일에 추가 (기존 파일에 이어쓰기)
        df.to_csv(file_name, mode='a', header=False, index=False)
        print(f"데이터가 '{file_name}' 파일에 추가되었습니다.")
    except Exception as e:
        print(f"데이터를 추가하는 도중 오류가 발생했습니다: {e}")

