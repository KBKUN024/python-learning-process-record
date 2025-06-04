"""
这个文件是一个比较简单的面向对象的例子，学生管理系统。
"""
from typing import Dict, Optional, Union
import json


class Student:
    """学生类"""

    def __init__(self, name: str, age: int, scores: Optional[Dict[str, float]] = None):
        self.name = name
        self.age = age
        self.scores = scores or {}

    def add_score(self, subject: str, score: float):
        """添加单科成绩"""
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在0-100之间")
        self.scores[subject] = score

    def get_average(self) -> float:
        """计算平均分"""
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)

    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "name": self.name,
            "age": self.age,
            "scores": self.scores,
            "average": self.get_average(),
        }


class ScoreManagement:
    """学生成绩管理系统 - 生产级别"""

    def __init__(self, system_name: str = "默认系统"):
        self.system_name = system_name
        self.students: Dict[str, Student] = {}
        print(f"创建学生管理系统: {system_name}")

    def add_student(
        self, name: str, age: int, scores: Optional[Dict[str, float]] = None
    ) -> bool:
        """添加学生"""
        try:
            if name in self.students:
                print(f"学生 {name} 已存在，更新信息")
            student = Student(name, age, scores)
            self.students[name] = student
            print(f"成功添加学生: {name}")
            return True
        except Exception as e:
            print(f"添加学生失败: {e}")
            return False

    def remove_student(self, name: str) -> bool:
        """删除学生"""
        if name in self.students:
            del self.students[name]
            print(f"已删除学生: {name}")
            return True
        else:
            print(f"学生 {name} 不存在")
            return False

    def get_student(self, name: str) -> Optional[Student]:
        """获取学生对象"""
        return self.students.get(name)

    def get_student_info(self, name: str) -> Optional[Dict]:
        """查询学生信息"""
        student = self.get_student(name)
        if student:
            info = student.to_dict()
            print(f"{name} 的详细信息: {info}")
            return info
        else:
            print(f"未找到学生: {name}")
            return None

    def calculate_average(self, name: str) -> Optional[float]:
        """计算学生平均分"""
        student = self.get_student(name)
        if student:
            avg = student.get_average()
            print(f"{name} 的平均分: {avg:.2f}")
            return avg
        else:
            print(f"未找到学生: {name}")
            return None

    def list_all_students(self):
        """列出所有学生"""
        if not self.students:
            print("暂无学生记录")
            return

        print(f"\n=== {self.system_name} 学生列表 ===")
        for name, student in self.students.items():
            print(f"  {name}: 年龄{student.age}, 平均分{student.get_average():.1f}")

    def get_top_students(self, n: int = 3) -> list:
        """获取成绩前N名学生"""
        if not self.students:
            return []

        sorted_students = sorted(
            self.students.values(), key=lambda s: s.get_average(), reverse=True
        )
        return sorted_students[:n]

    def export_to_json(self, filename: str) -> bool:
        """导出数据到JSON文件"""
        try:
            data = {
                "system_name": self.system_name,
                "students": {
                    name: student.to_dict() for name, student in self.students.items()
                },
            }
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"数据已导出到: {filename}")
            return True
        except Exception as e:
            print(f"导出失败: {e}")
            return False


# 演示使用
if __name__ == "__main__":
    print("=== 生产级别学生管理系统 ===")
    
    # 创建管理系统（只创建一次）
    class_name = input("请输入班级的名称: ")
    class_a = ScoreManagement(class_name)
    
    while True:
        print("\n=== 菜单 ===")
        print("1. 添加学生")
        print("2. 查询学生信息") 
        print("3. 计算学生平均分")
        print("4. 列出所有学生")
        print("5. 查看前三名")
        print("6. 导出数据")
        print("7. 退出")
        
        choice = input("请选择操作 (1-7): ").strip()
        
        if choice == "1":
            # 添加学生
            try:
                name = input("请输入学生姓名: ").strip()
                age = int(input("请输入学生年龄: ").strip())
                
                # 输入成绩（可选）
                has_scores = input("是否输入成绩？(y/n): ").strip().lower()
                scores = None
                
                if has_scores == 'y':
                    scores = {}
                    print("请输入成绩（输入空行结束）:")
                    while True:
                        subject = input("科目名称: ").strip()
                        if not subject:
                            break
                        try:
                            score = float(input(f"{subject}成绩: ").strip())
                            if 0 <= score <= 100:
                                scores[subject] = score
                            else:
                                print("成绩必须在0-100之间")
                        except ValueError:
                            print("请输入有效的数字")
                
                class_a.add_student(name, age, scores)
                
            except ValueError as e:
                print(f"输入错误: {e}")
            except Exception as e:
                print(f"添加学生时出错: {e}")
        
        elif choice == "2":
            # 查询学生信息
            name = input("请输入要查询的学生姓名: ").strip()
            class_a.get_student_info(name)
        
        elif choice == "3":
            # 计算学生平均分
            name = input("请输入要计算平均分的学生姓名: ").strip()
            class_a.calculate_average(name)
        
        elif choice == "4":
            # 列出所有学生
            class_a.list_all_students()
        
        elif choice == "5":
            # 查看前三名
            top_students = class_a.get_top_students(3)
            if top_students:
                print(f"\n前3名学生:")
                for i, student in enumerate(top_students, 1):
                    print(f"  第{i}名: {student.name} - {student.get_average():.1f}分")
            else:
                print("暂无学生数据")
        
        elif choice == "6":
            # 导出数据
            filename = input("请输入导出文件名 (默认: class_data.json): ").strip()
            if not filename:
                filename = "class_data.json"
            class_a.export_to_json(filename)
        
        elif choice == "7":
            # 退出
            print("谢谢使用！")
            break
        
        else:
            print("无效选择，请重新输入")
