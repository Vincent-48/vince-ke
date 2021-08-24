class mystring(str):
    def oma(self):
        return "it works"


from unittest.mock import patch
with patch("__main__.str", new=mystring):
    print(str("a").oma())
    print(str("a").rjust(6))
    print("a".rjust(6))