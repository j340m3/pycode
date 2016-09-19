from pycode.persistence import obtain,persist,count
import os
class TestPersistence(object):
    def test_import(self):
        samples = [
            {"x":1,"y":2,"z":3},
            {"x":4,"y":5,"z":6},
        ]
        try:
            persist("test.txt",samples[0],"w+")
            persist("test.txt",samples[1],"a+")
            assert "test.txt" in os.listdir(os.getcwd())
            res = obtain("test.txt")
            assert count("test.txt") == 3
        finally:
            if "test.txt" in os.listdir(os.getcwd()):
                os.remove("test.txt")

        assert len(res) == len(samples)
        for i in range(len(samples)):
            for j in samples[i].keys():
                assert j in res[i].keys()
                assert str(samples[i][j]) == res[i][j]
