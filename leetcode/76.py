def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""


assert minWindow(s='ADOBECODEBANC', t='ABC') == 'BANC'
