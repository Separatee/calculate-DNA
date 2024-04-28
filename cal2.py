from math import factorial
import time
import sys
def calculate_combinations(total_positions, max_a_t, max_g_c):
    # 初始化计数器
    count = 0

    # 遍历所有可能的A和T的数量
    for a_t in range(max_a_t + 1):
        for g_c in range(max_g_c + 1):
            if a_t + g_c <= total_positions:
                # 计算剩余的G和C的数量
                remaining = total_positions - (a_t + g_c)
                # 如果剩余的数量小于或等于G和C的最大数量，则计算组合数
                if remaining <= max_g_c:
                    count += factorial(total_positions) // (factorial(a_t) * factorial(g_c) * factorial(remaining))

    return count

# 总位置数为100，A和T的最大数量为30，G和C的最大数量为70
total_positions = 100
max_a_t = 30
max_g_c = 70


# 计算多项式系数
polynomial_coefficients = calculate_combinations(total_positions, max_a_t, max_g_c)

# 模拟进度条的函数
def fake_progress_bar(duration):
    for i in range(duration):
        sys.stdout.write('\r')
        sys.stdout.write(f"正在计算中,预计剩余时间: [{'=' * i}{' ' * (duration - i - 1)}] {i + 1}/{duration} seconds")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\n')

# 调用这个函数，暂停7秒
fake_progress_bar(7)
print(f"计算的结果是 {polynomial_coefficients} \n 用科学计数法表示约为 {polynomial_coefficients:3e}")

# ANSI转义序列
RED = "\033[1;31m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# 定义数字和当前世界人口
world_population = 7.8e9  # 78亿

# 计算倍数
multiple = polynomial_coefficients / world_population

# 打印结果
print(f"这个数大约是世界人口的 {RED} {multiple:.3e} {RESET} 倍.")
day_birth = 6300
day = polynomial_coefficients / day_birth
all_day_1_year = 365
year = day / all_day_1_year
print(f"全球平均每天有6300个新生儿，如果每个人都用这100个位点，大约那么能用 {RED} {year:.2e} 年 {RESET} .")
space_age = 1.38e10
num_by_space_age = day / space_age
print(f"还是不知道这玩意有多大？要知道，宇宙的目前的形成年龄为 {space_age:.2e} 年,所以这个数字大约是宇宙形成时间的{RED} {num_by_space_age:.3e} {RESET} 倍.足够用到 {YELLOW} 整个银河系不复存在 {RESET}.")
print("Powered By Sep.")