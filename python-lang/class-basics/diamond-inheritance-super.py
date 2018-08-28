class BaseClass:
     num_base_calls = 0
     def call_me(self):
         print("Calling method on Base Class")
         self.num_base_calls += 1
class LeftBaseClass(BaseClass):
     num_left_calls = 0
     def call_me(self):
         # call with super instead of BaseClass.call_me(self)
         super().call_me()
         print("Calling method on Left Class")
         self.num_left_calls += 1
class RightBaseClass(BaseClass):
     num_right_calls = 0
     def call_me(self):
         super().call_me()
         print("Calling method on Right Class")
         self.num_right_calls += 1
class SubClass(LeftBaseClass, RightBaseClass):
     num_sub_calls = 0
     def call_me(self):
         super().call_me()
         print("Calling method on Sub Class")
         self.num_sub_calls += 1
if __name__ == '__main__':
     s = SubClass()
     s.call_me()
 # shows that base calls is called twice.
     print("num_base_calls %s" % s.num_base_calls)

