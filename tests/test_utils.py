import unittest

from pycode.utils import Decorator


class TestDecorator(unittest.TestCase):
    def test_init(self):
        self.assertIsNotNone(Decorator())

    def test_class_without_args(self):
        @Decorator
        class A:
            def a(self):
                return 2
        a_inst = A()

        self.assertIsNotNone(a_inst)
        self.assertEqual(a_inst.__class__.__name__,"A")
        self.assertEqual(a_inst.a(),2)

    def test_method_without_args(self):
        @Decorator
        def A():
            return 3

        self.assertEqual(A(), 3)

    def test_arg_class_without_args(self):
        @Decorator
        class A:
            def __init__(self,b):
                self.b = b

            def a(self):
                return self.b

        a_inst = A(2)

        self.assertIsNotNone(a_inst)
        self.assertEqual(a_inst.__class__.__name__, "A")
        self.assertEqual(a_inst.a(), 2)

    def test_arg_method_without_args(self):
        @Decorator
        def A(a):
            return a

        self.assertEqual(A(3), 3)

    def test_class_with_args(self):
        @Decorator(1,k=2)
        class A:
            def a(self):
                return 2
        a_inst = A()

        self.assertIsNotNone(a_inst)
        self.assertEqual(a_inst.__class__.__name__,"A")
        self.assertEqual(a_inst.a(),2)

    def test_method_with_args(self):
        @Decorator(1,k=2)
        def A():
            return 3

        self.assertEqual(A(), 3)

    def test_arg_class_with_args(self):
        @Decorator(1,k=2)
        class A:
            def __init__(self, b):
                self.b = b

            def a(self):
                return self.b

        a_inst = A(2)

        self.assertIsNotNone(a_inst)
        self.assertEqual(a_inst.__class__.__name__, "A")
        self.assertEqual(a_inst.a(), 2)

    def test_arg_method_without_args(self):
        @Decorator(1,k=2)
        def A(a):
            return a

        self.assertEqual(A(3), 3)

    def test_callable_as_decorator_arg_in_function(self):
        def f(a):
            return a*2

        @Decorator(f, k=2)
        def A(a):
            return a

        self.assertEqual(A(3), 3)

    def test_callable_as_decorator_arg_in_class(self):
        def f(a):
            return a*2

        @Decorator(f, k=2)
        class A:
            def __init__(self, b):
                self.b = b

            def a(self):
                return self.b

        a_inst = A(2)

        self.assertIsNotNone(a_inst)
        self.assertEqual(a_inst.__class__.__name__, "A")
        self.assertEqual(a_inst.a(), 2)

    def test_callable_everywhere_in_function(self):
        def f(a):
            return a*2

        def ident(a):
            return a

        @Decorator(f, k=2)
        def A(a):
            return a

        self.assertEqual(A(ident(3)), 3)

    def test_callable_everywhere_in_class(self):
        def f(a):
            return a*2

        def g(a):
            return a

        @Decorator(f, k=2)
        class A:
            def __init__(self, b):
                self.b = b

            def a(self):
                return self.b(2)

        a_inst = A(g)

        self.assertIsNotNone(a_inst)
        self.assertEqual(a_inst.__class__.__name__, "A")
        self.assertEqual(a_inst.a(), 2)

if __name__ == "__main__":
    unittest.main()
