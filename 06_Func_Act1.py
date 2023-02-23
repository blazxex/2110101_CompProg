def is_undergrad(sid):
    grad = ['0','3','4']
    if sid[2] in grad:
        return True
    return False
def get_faculty(sid):
    fac = sid[-2:]
    if fac =='21':
        return 'ENG'
    elif fac =='22':
        return'ART'
    elif fac == '23':
        return 'SCI'
    return 'OTHER'

def get_status(sid):
    if is_undergrad(sid):
        return ['U',get_faculty(sid)]
    return ['G',get_faculty(sid)]
        
    
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader