import sys
import importlib.util
import re

def load_module():
    """动态加载学生模块"""
    try:
        spec = importlib.util.spec_from_file_location("student_module", "main.py")
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)
        return student_module
    except Exception as e:
        print(f"❌ 导入学生模块失败: {e}")
        return None

def test_prime_list():
    """主测试函数"""
    module = load_module()
    if not module or not hasattr(module, 'PrimeList'):
        print("❌ 未找到 PrimeList 函数")
        return False
    
    PrimeList = module.PrimeList
    
    test_cases = [
        # 边界情况
        (-5, ""),           # 负数
        (0, ""),            # 零
        (1, ""),            # 1
        (2, ""),            # 2（小于2的质数不存在）
        
        # 小范围测试
        (3, "2"),           # 3
        (10, "2 3 5 7"),    # 10
        (20, "2 3 5 7 11 13 17 19"),  # 20
        
        # 中等范围测试
        (30, "2 3 5 7 11 13 17 19 23 29"),  # 30
        (50, "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47"),  # 50
        
        # 大数测试
        (100, "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97"),  # 100
        
        # 特殊值
        (10000, None)       # 验证大数正确性（不验证具体值）
    ]
    
    passed = 0
    total = len(test_cases)
    
    for N, expected in test_cases:
        try:
            result = PrimeList(N)
            
            # 验证返回类型
            if not isinstance(result, str):
                print(f"❌ 测试失败: N={N}")
                print(f"   预期: 字符串 | 实际: {type(result)}")
                continue
            
            # 验证大数情况
            if expected is None and N > 1000:
                # 验证格式和基本正确性
                if not re.match(r"^\d+( \d+)*$", result) or "1" in result:
                    print(f"❌ 测试失败: N={N} (大数验证)")
                    print("   输出格式错误或包含1")
                else:
                    print(f"✅ 测试通过: N={N} (大数验证)")
                    passed += 1
                continue
            
            # 验证具体值
            if result == expected:
                print(f"✅ 测试通过: N={N}")
                passed += 1
            else:
                print(f"❌ 测试失败: N={N}")
                print(f"   预期: '{expected}'")
                print(f"   实际: '{result}'")
                
        except Exception as e:
            print(f"❌ 测试异常: N={N}")
            print(f"   异常: {e}")
    
    print(f"\n测试结果: {passed}/{total} 通过")
    if passed == total:
        print("🎉 所有测试通过!")
        return True
    else:
        print("💥 存在未通过的测试")
        return False

if __name__ == "__main__":
    success = test_prime_list()
    sys.exit(0 if success else 1)
