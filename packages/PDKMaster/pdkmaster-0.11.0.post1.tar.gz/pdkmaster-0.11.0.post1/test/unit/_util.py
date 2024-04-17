# SPDX-License-Identifier: AGPL-3.0-or-later OR GPL-2.0-or-later OR CERN-OHL-S-2.0+ OR Apache-2.0
# type: ignore
import unittest

from pdkmaster import _util

class UtilTest(unittest.TestCase):
    def test_i2f_recursive(self):
        f = _util.i2f_recursive(2)
        self.assertIsInstance(f, float)
        self.assertAlmostEqual(f, 2.0, 12)

        t = _util.i2f_recursive((range(3), 3, 4.0))
        self.assertIsInstance(t, tuple)
        self.assertAlmostEqual(t[0][0], 0.0, 12)
        self.assertAlmostEqual(t[0][2], 2.0, 12)
        self.assertAlmostEqual(t[1], 3.0, 12)
        self.assertAlmostEqual(t[2], 4.0, 12)

    def test_is_iterable(self):
        self.assertEqual(_util.is_iterable(None), False)
        self.assertEqual(_util.is_iterable(1), False)
        self.assertEqual(_util.is_iterable(1.0), False)
        self.assertEqual(_util.is_iterable(range(2)), True)
        self.assertEqual(_util.is_iterable((1, "a")), True)
        self.assertEqual(_util.is_iterable({0}), True)
        self.assertEqual(_util.is_iterable("a"), False)

    def test_get_nth_of(self):
        self.assertEqual(_util.get_nth_of(range(5), n=2), 2)
        with self.assertRaises(StopIteration):
            _util.get_nth_of(range(2), n=3)

    def test_first(self):
        self.assertEqual(_util.get_first_of(range(5)), 0)
        with self.assertRaises(StopIteration):
            _util.get_first_of(tuple())

    def test_last(self):
        self.assertEqual(_util.get_last_of(range(2)), 1)
        with self.assertRaises(StopIteration):
            _util.get_last_of({})

    def test_strip_literal(self):
        self.assertEqual(_util.strip_literal('"Yoh"'), 'Yoh')
        self.assertEqual(_util.strip_literal("'Yoh'"), "'Yoh'")
        self.assertEqual(_util.strip_literal('"Yoh"'), 'Yoh')
        self.assertEqual(_util.strip_literal('"Yoh'), '"Yoh')
        self.assertEqual(_util.strip_literal('Yoh"'), 'Yoh"')

    def test_extendedlist(self):
        l = _util.ExtendedList[float]()
        self.assertEqual(list(l + 3.0), [3.0])
        self.assertEqual(list(l + [2.0, 3.0]), [2.0, 3.0])

        l += 1.0
        l += [2.0, 3.0]
        self.assertEqual(list(l), [1.0, 2.0, 3.0])

        self.assertEqual(l.pop(1), 2.0)
        self.assertEqual(list(l), [1.0, 3.0])

        del l[1]
        self.assertEqual(list(l), [1.0])

        l *= 2
        self.assertEqual(list(l), [1.0, 1.0])

        l.insert(0, 0.0)
        self.assertEqual(list(l), [0.0, 1.0, 1.0])

        l.remove(1.0)
        self.assertEqual(list(l), [0.0, 1.0])

        l.reverse()
        self.assertEqual(list(l), [1.0, 0.0])

        l.sort()
        self.assertEqual(list(l), [0.0, 1.0])

        l.append(2.0)
        self.assertEqual(list(l), [0.0, 1.0, 2.0])

        l._reorder_(neworder=[2, 1, 0])
        self.assertEqual(list(l), [2.0, 1.0, 0.0])

        with self.assertRaises(ValueError):
            # indices mismatch
            l._reorder_(neworder=[1, 0])
        with self.assertRaises(TypeError):
            # hash for non-frozen TypedList
            hash(l)

        l._freeze_()
        self.assertEqual(hash(l), hash(tuple(l)))
        with self.assertRaises(TypeError):
            del l[0]
        with self.assertRaises(TypeError):
            l += 10.0
        with self.assertRaises(TypeError):
            l *= 2
        with self.assertRaises(TypeError):
            l[0] = 2.0
        with self.assertRaises(TypeError):
            l.append(4.0)
        with self.assertRaises(TypeError):
            l.clear()
        with self.assertRaises(TypeError):
            l.extend([3.0, 4.0])
        with self.assertRaises(TypeError):
            l.insert(0, 0.0)
        with self.assertRaises(TypeError):
            l.pop()
        with self.assertRaises(TypeError):
            l.insert(0, 0.0)
        with self.assertRaises(TypeError):
            l.remove(1.0)
        with self.assertRaises(TypeError):
            l.reverse()
        with self.assertRaises(TypeError):
            l.sort()
        with self.assertRaises(TypeError):
            l._reorder_(neworder=[2, 1, 0])
    
    def test_extendedlistmapping(self):
        class C:
            def __init__(self, *, name: str) -> None:
                self.name=name

        class MyList(_util.ExtendedListMapping[C, str]):
            @property
            def _index_attribute_(self) -> str:
                return "name"

        with self.assertRaises(ValueError):
            l = MyList("error")

        cs = (C(name="1"), C(name="2"), C(name="3"), C(name="4"), C(name="5"))
        l = MyList(cs)
        self.assertEqual(tuple(l), cs)
        self.assertEqual(l[0], cs[0])
        self.assertEqual(tuple(l[1:]), cs[1:])

        c = C(name="6")
        cs += (c,)
        l[c.name] = c
        self.assertEqual(tuple(l), cs)

        cs = cs[:-1]
        del l[5]
        self.assertEqual(tuple(l), cs)

        cs = cs[:-1]
        del l["5"]
        self.assertEqual(tuple(l), cs)

        self.assertEqual(l.pop(), cs[-1])
        cs = cs[:-1]
        self.assertEqual(tuple(l), cs)

        self.assertEqual(l.pop("1"), cs[0])
        cs = cs[1:]
        self.assertEqual(tuple(l), cs)

        self.assertEqual(l.pop(0), cs[0])
        cs = cs[1:]
        self.assertEqual(tuple(l), cs)

        c = C(name="1")
        cs = (c, *cs)
        l.insert(0, c)
        self.assertEqual(tuple(l), cs)

        self.assertEqual(set(l.values()), set(cs))

        with self.assertRaises(KeyError):
            # wrong index type just leads to key not present
            del l[3.0]
        with self.assertRaises(AttributeError):
            # wrong element type so it will try to access name attribute
            l[0] = "error"

        c = C(name="6")
        cs = (*cs, c)
        l += c
        self.assertEqual(tuple(l), cs)

        order = tuple(reversed(range(len(l))))
        cs = tuple(cs[n] for n in order)
        l._reorder_(neworder=order)
        self.assertEqual(tuple(l), cs)

        l.clear()
        self.assertEqual(len(l), 0)

        with self.assertRaises(IndexError):
            # wrong index
            l[0]
        with self.assertRaises(NotImplementedError):
            l.popitem()
        with self.assertRaises(NotImplementedError):
            l.update({"5": C(name="5")})

        l._freeze_()
        # Changing a frozen list
        c = C(name="6")
        with self.assertRaises(TypeError):
            l[c.name] = c
        with self.assertRaises(TypeError):
            del l[5]
        with self.assertRaises(TypeError):
            l.pop()
        with self.assertRaises(TypeError):
            l.insert(0, c)
        with self.assertRaises(TypeError):
            l.clear()
        with self.assertRaises(TypeError):
            l += c
        with self.assertRaises(TypeError):
            order = tuple(reversed(range(len(l))))
            l._reorder_(neworder=order)

    def test_liststrmappingoverride(self):
        class C1:
            def __init__(self, *, name: str) -> None:
                self.name = name

        class C2(C1):
            pass

        MyList1 = _util.ExtendedListStrMapping[C1]
        class MyList2(_util.ListStrMappingOverride[C2], MyList1):
            pass

        MyList1()
        MyList2()

        cs = (C2(name="0"), C2(name="1"), C2(name="2"), C2(name="3"))
        l = MyList2(cs)
        self.assertEqual(tuple(l), cs)
        self.assertEqual(l[0], cs[0])

        l[0] = cs[0]
        self.assertEqual(l[0], cs[0])

        cs = cs[1:]
        del l[0]
        self.assertEqual(l[0], cs[0])

        self.assertEqual(l.pop(), cs[-1])
        cs = cs[:-1]
        self.assertEqual(l[0], cs[0])

        c = C2(name="4")
        with self.assertRaises(NotImplementedError):
            l.update({"4": c})

        self.assertEqual(l.index(cs[0]), 0)

        c = C2(name="-1")
        cs = (c, *cs)
        l.insert(0, c)
        self.assertEqual(l[0], cs[0])
