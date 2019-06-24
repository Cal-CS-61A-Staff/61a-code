from __future__ import print_function
import code
import functools
import inspect
import re
import signal
import sys
import math
import sys
import numbers
import scheme
import math
import numbers
import operator
import sys
import scheme
import itertools
import string
import sys
import tokenize
'o_81pkm6_FCJd33M2HqNrj'

def CK0_s(Y__t):
    'd4C9g13q2prL7_Q_T6jo_Q1_o'
    if (inspect.stack()[(((-24 + 90) + (-11 + -4)) + ((-80 + 94) + (-93 + 29)))][int((((-0.8894037474059218 + 0.7207172922303631) + (-0.585126543003851 + 0.8372680766498214)) * int((0.6846980092618451 * 0))))].f_locals[(('' + ('__' + 'n')) + (('' + 'ame') + ('' + '__')))] == ((('' + '__m') + ('' + 'ai')) + (str() + ('' + 'n__')))):
        xP7_9BaX = sys.argv[(((14 + 20) + (-119 + 50)) + ((-99 + 82) + (26 + 27))):]
        Y__t(*xP7_9BaX)
    return Y__t
V2F7 = str()

def W3o6(Y__t):
    'lq6Jj_d3H9E2WIa_0UU8M'

    @functools.wraps(Y__t)
    def c3WB850_(*xP7_9BaX, **X9Vq2):
        global V2F7
        ZZht_18__ = [repr(uWK066) for uWK066 in xP7_9BaX]
        ZZht_18__ += [((repr(c6O_1MTVr) + chr(((-44 + 43) + (156 + -94)))) + repr(N6g0t8t)) for (c6O_1MTVr, N6g0t8t) in X9Vq2.items()]
        A4Y7(((str() + ('{' + ('0' + '}({1})'))).format(Y__t.__name__, (chr((-14 + 58)) + chr(32)).join(ZZht_18__)) + chr(58)))
        V2F7 += (str() + ('' + ('' + '    ')))
        try:
            q1Gj04i = Y__t(*xP7_9BaX, **X9Vq2)
            V2F7 = V2F7[:(- (((253 + -83) + (-165 + 98)) + ((-198 + 31) + (-9 + 77))))]
        except Exception as uWK066:
            A4Y7((Y__t.__name__ + ((chr(32) + ('exite' + 'd via except')) + ('i' + ('' + 'on')))))
            V2F7 = V2F7[:(- (((-49 + -19) + (1 + -29)) + ((154 + 27) + (-96 + 15))))]
            raise
        A4Y7(((('' + '{0}({1') + ('' + '}) ')) + (('-' + '> {') + ('' + '2}'))).format(Y__t.__name__, (str() + (',' + ' ')).join(ZZht_18__), q1Gj04i))
        return q1Gj04i
    return c3WB850_

def A4Y7(Ie59t6):
    'W95w28a75_E91_y5_bm11'
    print((V2F7 + re.sub(chr((16 + -6)), (chr((11 + -1)) + V2F7), str(Ie59t6))))

def rt3__9():
    'B9j13V7w2tk_Nljc0u_t578'
    c0iZ3_ = inspect.stack()[(((23 + 27) + (-17 + 8)) + ((54 + -81) + (3 + -16)))]
    A4Y7(((('Curre' + 'n') + ('t line: ' + 'File "{f[')) + (('1]}", line {f[2]}, in {f' + '[') + ('' + '3]}'))).format(f=c0iZ3_))

def r0_1Ez_70(HVg58Yd=None):
    'P5_52_gNlqDB3D28rG9z_BFGJ'
    c0iZ3_ = inspect.currentframe().f_back
    G9_9 = c0iZ3_.f_globals.copy()
    G9_9.update(c0iZ3_.f_locals)

    def h6MYP51Z_(signum, c0iZ3_):
        print()
        exit(int((((-0.41855498874079555 + 0.7201799846155581) + (0.3481217997403183 + 0.05016554010245722)) * 0)))
    signal.signal(signal.SIGINT, h6MYP51Z_)
    if (not HVg58Yd):
        (g8_c06K, x3f_w, aYu_, g8_c06K, g8_c06K, g8_c06K) = inspect.stack()[(((-176 + 89) + (118 + -39)) + ((160 + -61) + (-122 + 32)))]
        HVg58Yd = ((('Interacting at File "{0}' + '",') + (' line' + ' ')) + (('{1' + '} ') + '\n')).format(x3f_w, aYu_)
        HVg58Yd += ((('    Unix:    <' + 'Cont') + ('rol>-' + 'D cont')) + (('inu' + 'es') + (' the program;' + ' \n')))
        HVg58Yd += ((('' + '    W') + ('indows' + ':')) + ((' <Control>-Z <Enter> co' + 'ntinues the pro') + ('gram' + '; \n')))
        HVg58Yd += ((chr(32) + (' ' + '  ')) + (('exit() or <Control>-C exits t' + 'he pr') + ('ogr' + 'am')))
    code.interact(HVg58Yd, None, G9_9)
'P9BiocX0oT1_1oYI41_009G7'
if (sys.version_info[int(((-0.2486400731278614 + 0.755749296849583) * int((0.006649010149037071 * 0))))] < (((205 + -60) + (-161 + 84)) + ((-226 + 83) + (37 + 41)))):

    def input(hrx_gaO0):
        sys.stderr.write(hrx_gaO0)
        sys.stderr.flush()
        aYu_ = sys.stdin.readline()
        if (not aYu_):
            raise EOFError()
        return aYu_.rstrip(('' + ('\r' + chr(10))))

class kF4Qr(object):
    'gDQ9_A9Ae9___7E324_359Iq0xIoT'

    def __init__(OnB2B__, bYtOI):
        OnB2B__.index = int((0.6512246174494061 * 0))
        OnB2B__.c9LiI29Z7 = []
        OnB2B__.bYtOI = bYtOI
        OnB2B__.current_line = ()
        OnB2B__.current()

    def JNZ6wu7_(OnB2B__):
        'a22__830_b70CT7_5e_j'
        current = OnB2B__.current()
        OnB2B__.index += (((-141 + 52) + (31 + -9)) + ((35 + 33) + int((0.3302772639594287 * 0))))
        return current

    def current(OnB2B__):
        'LL7F44n9_270b6489QD56_2_nW9'
        while (not OnB2B__.F49_454J):
            OnB2B__.index = int((((-0.15880976717350093 + 0.41702965236676603) + (0.664887633220133 + 0.07002061505037538)) * int(((0.5456981537306473 + 0.3061243976352531) * int((0.7289715382116503 * 0))))))
            try:
                OnB2B__.current_line = next(OnB2B__.bYtOI)
                OnB2B__.c9LiI29Z7.append(OnB2B__.current_line)
            except StopIteration:
                OnB2B__.current_line = ()
                return None
        return OnB2B__.current_line[OnB2B__.index]

    @property
    def F49_454J(OnB2B__):
        return (OnB2B__.index < len(OnB2B__.current_line))

    def __str__(OnB2B__):
        'nl_UF69gQ_5Z9f9485J35A1'
        AE7F = len(OnB2B__.c9LiI29Z7)
        HVg58Yd = (((chr((223 + -100)) + (('0' + ':') + chr(62))) + str((math.floor(math.log10(AE7F)) + (((177 + -23) + (-65 + -4)) + ((82 + -77) + (-178 + 89)))))) + ('' + (str() + ('' + '}: '))))
        mt_q_ = str()
        for K_2TKRT8 in range(max(int(((-0.41346554106508115 + 0.8629904140587854) * int((0.6681469557304683 * 0)))), (AE7F - (((52 + 27) + (-135 + 86)) + ((41 + -86) + (32 + -13))))), (AE7F - (((60 + -87) + (-105 + 93)) + ((-11 + 27) + (104 + -80))))):
            mt_q_ += ((HVg58Yd.format((K_2TKRT8 + (int(((0.6255318384169437 + 0.3044442768702521) * int((0.36434442327603245 * 0)))) + ((-1 + 97) + (-79 + -16))))) + ' '.join(map(str, OnB2B__.c9LiI29Z7[K_2TKRT8]))) + chr(10))
        mt_q_ += HVg58Yd.format(AE7F)
        mt_q_ += chr((-7 + 39)).join(map(str, OnB2B__.current_line[:OnB2B__.index]))
        mt_q_ += (str() + ((' >' + '>') + chr(32)))
        mt_q_ += chr((96 + -64)).join(map(str, OnB2B__.current_line[OnB2B__.index:]))
        return mt_q_.strip()
try:
    import readline
except:
    pass

class Qr_2(object):
    'SB_4L2_822C0___0Xd_p'

    def __init__(OnB2B__, hrx_gaO0):
        OnB2B__.hrx_gaO0 = hrx_gaO0

    def __iter__(OnB2B__):
        while True:
            (yield input(OnB2B__.hrx_gaO0))
            OnB2B__.hrx_gaO0 = (chr((37 + -5)) * len(OnB2B__.hrx_gaO0))

class R2Eg(object):
    'iNbr0qASbm79u2_4h_OvB'

    def __init__(OnB2B__, c9LiI29Z7, hrx_gaO0, j12_S3=';'):
        OnB2B__.c9LiI29Z7 = c9LiI29Z7
        OnB2B__.hrx_gaO0 = hrx_gaO0
        OnB2B__.j12_S3 = j12_S3

    def __iter__(OnB2B__):
        while OnB2B__.c9LiI29Z7:
            aYu_ = OnB2B__.c9LiI29Z7.pop(0).strip(chr(((-96 + 67) + (-54 + 93))))
            if ((OnB2B__.hrx_gaO0 is not None) and (aYu_ != str()) and (not aYu_.lstrip().startswith(OnB2B__.j12_S3))):
                print((OnB2B__.hrx_gaO0 + aYu_))
                OnB2B__.hrx_gaO0 = (chr(((-95 + 80) + (55 + -8))) * len(OnB2B__.hrx_gaO0))
            (yield aYu_)
        raise EOFError
'A_J2_1VB64q69832_gX1019_6ER'

class Pair(object):
    'EsY73nX04N_0__pU2T_14382T'

    def __init__(OnB2B__, first, second):
        if ((not scheme.DOTS_ARE_CONS) and (not l3T9671_(second))):
            raise Y6__(((('cdr' + ' can') + (' onl' + 'y ')) + (('be a pair, nil, or a promi' + 'se') + (' b' + 'ut was {}'))).format(second))
        OnB2B__.first = first
        OnB2B__.second = second

    def __repr__(OnB2B__):
        return (('' + ('P' + 'air(')) + (('' + '{0}, {') + ('1}' + ')'))).format(repr(OnB2B__.first), repr(OnB2B__.second))

    def __str__(OnB2B__):
        mt_q_ = (chr(((107 + -1) + (-26 + -40))) + repl_str(OnB2B__.first))
        second = OnB2B__.second
        while isinstance(second, Pair):
            mt_q_ += (' ' + repl_str(second.first))
            second = second.second
        if (second is not nil):
            mt_q_ += ((str() + (('' + ' .') + chr(32))) + repl_str(second))
        return (mt_q_ + ')')

    def __len__(OnB2B__):
        (AE7F, second) = ((((70 + -46) + (-69 + 92)) + ((-75 + 40) + (85 + -96))), OnB2B__.second)
        while isinstance(second, Pair):
            AE7F += (((90 + -45) + (-29 + 35)) + ((-114 + 21) + (130 + -87)))
            second = second.second
        if (second is not nil):
            raise TypeError(((('length attempte' + 'd on i') + ('m' + 'prop')) + (('er' + ' ') + ('li' + 'st'))))
        return AE7F

    def __eq__(OnB2B__, t8_pEK):
        if (not isinstance(t8_pEK, Pair)):
            return False
        return ((OnB2B__.first == t8_pEK.first) and (OnB2B__.second == t8_pEK.second))

    def map(OnB2B__, Y__t):
        'qw0sswjw7f_8f4_k62_5'
        rWd6m6L8_ = Y__t(OnB2B__.first)
        if ((OnB2B__.second is nil) or isinstance(OnB2B__.second, Pair)):
            return Pair(rWd6m6L8_, OnB2B__.second.map(Y__t))
        else:
            raise TypeError(((('ill-fo' + 'rmed li') + ('s' + 't (cdr is ')) + (('' + 'a pro') + ('mise' + ')'))))

class nil(object):
    'n6mO3_e62WyI_36l__8bPN0'

    def __repr__(OnB2B__):
        return ((chr(110) + chr(105)) + 'l')

    def __str__(OnB2B__):
        return ('(' + chr((56 + -15)))

    def __len__(OnB2B__):
        return int(((0.32304202255546965 + 0.5953862942643868) * 0))

    def map(OnB2B__, Y__t):
        return OnB2B__
nil = nil()

class e7__HV8():
    'l2rX724G0t_38kM9Tyco_8'

    def __init__(OnB2B__, Ibi_X7P):
        if (not L__2d69(Ibi_X7P)):
            raise SyntaxError(((chr(105) + ('nvalid variadic symbol: (' + '. {0')) + (chr(125) + ')')).format(Ibi_X7P))
        OnB2B__.Ibi_X7P = Ibi_X7P

    def __repr__(OnB2B__):
        return (((('(v' + 'ar') + ('iad' + 'ic')) + ((' %' + 's') + ')')) % OnB2B__.Ibi_X7P)
j_k6 = {
    chr(39): ((str() + ('qu' + 'o')) + (str() + ('' + 'te'))),
    chr(((190 + -17) + (-33 + -44))): (('q' + ('u' + 'asiq')) + (('u' + 'o') + ('' + 'te'))),
    (chr((-1 + 45)) + chr(64)): ((('' + 'unq') + ('uo' + 'te-')) + (('spl' + 'i') + ('c' + 'ing'))),
    chr(((-24 + 99) + (-23 + -8))): ('u' + (('nqu' + 'o') + ('' + 'te'))),
}

def K5_e(G3_91o4):
    'j0_64r961sjLLR5tN07j_r_Ry7XF6'
    if (G3_91o4.current() is None):
        raise EOFError
    to7m1Mu_W = G3_91o4.JNZ6wu7_()
    if (to7m1Mu_W == (chr((149 + -39)) + ('' + ('' + 'il')))):
        return nil
    elif (to7m1Mu_W == chr(((-51 + 63) + (11 + 17)))):
        return KA2R7_2(G3_91o4)
    elif (to7m1Mu_W in j_k6):
        return Pair(j_k6[to7m1Mu_W], Pair(K5_e(G3_91o4), nil))
    elif ((to7m1Mu_W == chr(46)) and (not scheme.DOTS_ARE_CONS)):
        D8Ec4_01 = K5_e(G3_91o4)
        return e7__HV8(D8Ec4_01)
    elif (to7m1Mu_W not in GF49L):
        return to7m1Mu_W
    else:
        raise SyntaxError(((str() + ('une' + 'xpected ')) + (('token: ' + '{0') + '}')).format(to7m1Mu_W))

def KA2R7_2(G3_91o4):
    'v_DI_e_7EX6855yBKX1_'
    try:
        if (G3_91o4.current() is None):
            raise SyntaxError(((('u' + 'nex') + 'p') + ('' + ('ec' + 'ted end of file'))))
        elif (G3_91o4.current() == chr(((82 + -75) + (76 + -42)))):
            G3_91o4.JNZ6wu7_()
            return nil
        elif ((G3_91o4.current() == chr(((-61 + 64) + (75 + -32)))) and scheme.DOTS_ARE_CONS):
            G3_91o4.JNZ6wu7_()
            D8Ec4_01 = K5_e(G3_91o4)
            if (G3_91o4.current() is None):
                raise SyntaxError(((('unexp' + 'e') + ('cted e' + 'n')) + (('d ' + 'of') + (' f' + 'ile'))))
            if (G3_91o4.JNZ6wu7_() != chr((133 + -92))):
                raise SyntaxError((('e' + ('' + 'xp')) + (('ected one elemen' + 't af') + ('ter' + ' .'))))
            return D8Ec4_01
        else:
            first = K5_e(G3_91o4)
            b_fb7 = KA2R7_2(G3_91o4)
            return Pair(first, b_fb7)
    except EOFError:
        raise SyntaxError(((chr(117) + ('nexpected ' + 'en')) + (chr(100) + (' o' + 'f file'))))

def iH5vN2j02(hrx_gaO0='scm> '):
    'JB__Yd__b1Rs96DMY_762F____o'
    return kF4Qr(g8_Oo(Qr_2(hrx_gaO0)))

def yo15431(c9LiI29Z7, hrx_gaO0='scm> ', v4zri=False):
    'Yl__87A_7737I_P1O_C_____1F5f'
    if v4zri:
        v_B2_G = c9LiI29Z7
    else:
        v_B2_G = R2Eg(c9LiI29Z7, hrx_gaO0)
    return kF4Qr(g8_Oo(v_B2_G))

def J_sul8lp(aYu_):
    'feI9XO382x87_O21lhHY4dk_'
    return K5_e(kF4Qr(g8_Oo([aYu_])))

def repl_str(to7m1Mu_W):
    'z22o4i5P1__lK_iG3ev6Bw17824au'
    if (to7m1Mu_W is True):
        return ('#' + chr((211 + -95)))
    if (to7m1Mu_W is False):
        return (str() + ('#' + chr(102)))
    if (to7m1Mu_W is None):
        return (('u' + ('' + 'nde')) + (('fi' + 'n') + ('e' + 'd')))
    if (isinstance(to7m1Mu_W, numbers.Number) and (not isinstance(to7m1Mu_W, numbers.Integral))):
        return repr(to7m1Mu_W)
    return str(to7m1Mu_W)

def Z_Q59j():
    'A4Gz__tj8cB89rA__v__91_HI1_M'
    while True:
        try:
            G3_91o4 = iH5vN2j02(((('' + 're') + 'a') + ('' + ('d>' + ' '))))
            while G3_91o4.F49_454J:
                qXk_8l_ = K5_e(G3_91o4)
                if (qXk_8l_ == ((('e' + 'x') + 'i') + chr((108 + 8)))):
                    print()
                    return
                print(('s' + (('t' + 'r') + (' ' + ':'))), qXk_8l_)
                print((str() + (('r' + 'e') + ('p' + 'r:'))), repr(qXk_8l_))
        except (SyntaxError, ValueError) as s_1_:
            print((type(s_1_).__name__ + chr((22 + 36))), s_1_)
        except (KeyboardInterrupt, EOFError):
            print()
            return

def CK0_s(*xP7_9BaX):
    if (len(xP7_9BaX) and (((str() + ('' + '--re')) + (chr(112) + 'l')) in xP7_9BaX)):
        Z_Q59j()
'Q0771oN2_b0N_4halVO_0HFqJ40e'
try:
    import turtle
    import tkinter
except:
    print(((('warni' + 'n') + ('g: could not' + ' import ')) + (('the turtl' + 'e ') + ('' + 'module.'))), file=sys.stderr)

class Y6__(Exception):
    'As_Aw_7_9E3_Vf1D9aOP'
Ky5Q00 = []

def gQ5Y(*I3G__m37):
    'Ur3n_LxWC19f0ro6_k__'

    def add(Y__t):
        for V_6_ in I3G__m37:
            Ky5Q00.append((V_6_, Y__t, I3G__m37[int((((-1.0388495850687847 + 0.6206121460630394) + (0.5204817446610616 + 0.1230861678542714)) * 0))]))
        return Y__t
    return add

def mA79m(to7m1Mu_W, F_4rA_7K, c6O_1MTVr, V_6_):
    'E9p_f0v_cDeLD_Wp67S2W7_1Uv_'
    if (not F_4rA_7K(to7m1Mu_W)):
        HVg58Yd = ((('argument {0' + '} of {1') + ('} has wro' + 'ng')) + ((' t' + 'yp') + ('e ({2}' + ')')))
        raise Y6__(HVg58Yd.format(c6O_1MTVr, V_6_, type(to7m1Mu_W).__name__))
    return to7m1Mu_W

@gQ5Y((str() + (('b' + 'oolean') + '?')))
def B3np70_Yq(O1J7eT202):
    return ((O1J7eT202 is True) or (O1J7eT202 is False))

def SheK6O_6(to7m1Mu_W):
    'ML__1_0tBX_51XH3a8Ef4WH_25'
    return (to7m1Mu_W is not False)

def wJ98___(to7m1Mu_W):
    'XF72Q3_2_iB94pe9_1t3D249A'
    return (to7m1Mu_W is False)

@gQ5Y((('' + ('' + 'no')) + chr((211 + -95))))
def J_48(O1J7eT202):
    return (not SheK6O_6(O1J7eT202))

@gQ5Y(((str() + ('eq' + 'ual')) + chr((116 + -53))))
def a30_(O1J7eT202, I_W9Y_V7_):
    if (b4I_37_0C(O1J7eT202) and b4I_37_0C(I_W9Y_V7_)):
        return (a30_(O1J7eT202.first, I_W9Y_V7_.first) and a30_(O1J7eT202.second, I_W9Y_V7_.second))
    elif (e4W5_t2_3(O1J7eT202) and e4W5_t2_3(I_W9Y_V7_)):
        return (O1J7eT202 == I_W9Y_V7_)
    else:
        return ((type(O1J7eT202) == type(I_W9Y_V7_)) and (O1J7eT202 == I_W9Y_V7_))

@gQ5Y((chr((48 + 53)) + ('q' + chr(63))))
def W68844GZ_(O1J7eT202, I_W9Y_V7_):
    if (e4W5_t2_3(O1J7eT202) and e4W5_t2_3(I_W9Y_V7_)):
        return (O1J7eT202 == I_W9Y_V7_)
    elif (L__2d69(O1J7eT202) and L__2d69(I_W9Y_V7_)):
        return (O1J7eT202 == I_W9Y_V7_)
    else:
        return (O1J7eT202 is I_W9Y_V7_)

@gQ5Y(((('' + 'pa') + 'i') + ('r' + chr(63))))
def b4I_37_0C(O1J7eT202):
    return isinstance(O1J7eT202, Pair)

@gQ5Y((chr((117 + -2)) + (('' + 'cheme-') + ('vali' + 'd-cdr?'))))
def l3T9671_(O1J7eT202):
    return (b4I_37_0C(O1J7eT202) or r_l4(O1J7eT202) or A1t_3(O1J7eT202))

@gQ5Y((('' + ('prom' + 'is')) + ('e' + '?')))
def A1t_3(O1J7eT202):
    return (type(O1J7eT202).__name__ == ('P' + (('' + 'romis') + 'e')))

@gQ5Y(((chr(102) + chr(111)) + (('r' + 'c') + 'e')))
def Xw_5Sdk_Z(O1J7eT202):
    mA79m(O1J7eT202, A1t_3, 0, ((('' + 'pro') + ('' + 'mi')) + ('' + ('s' + 'e'))))
    return O1J7eT202.h4r_Rq()

@gQ5Y((('c' + 'd') + (('' + 'r-s') + ('trea' + 'm'))))
def qR39(O1J7eT202):
    mA79m(O1J7eT202, (lambda O1J7eT202: (b4I_37_0C(O1J7eT202) and A1t_3(O1J7eT202.second))), int((((-1.0398674848263423 + 0.7528177787850443) + (0.35075941994236914 + 0.02183633333453805)) * int(((0.4881818418211251 + 0.4648583518900037) * 0)))), (str() + (('' + 'cdr-s') + ('t' + 'ream'))))
    return Xw_5Sdk_Z(O1J7eT202.second)

@gQ5Y(((('n' + 'u') + 'l') + (chr(108) + chr(63))))
def r_l4(O1J7eT202):
    return (O1J7eT202 is nil)

@gQ5Y(((str() + ('l' + 'i')) + (chr(115) + ('t' + '?'))))
def SjS5gc8(O1J7eT202):
    'X7__AIB_aO_7N7_9761a'
    while (O1J7eT202 is not nil):
        if (not isinstance(O1J7eT202, Pair)):
            return False
        O1J7eT202 = O1J7eT202.second
    return True

@gQ5Y((('l' + chr(101)) + (chr(110) + ('' + 'gth'))))
def Z2n0do45A(O1J7eT202):
    mA79m(O1J7eT202, SjS5gc8, int(((0.2085812968065648 + 0.034387653655436945) * int((0.46856675122775193 * 0)))), ('l' + (('en' + 'g') + ('' + 'th'))))
    if (O1J7eT202 is nil):
        return int(((0.11029281373299082 + 0.44673908771571924) * int((0.4538652443915544 * 0))))
    return len(O1J7eT202)

@gQ5Y((chr((180 + -81)) + (str() + ('o' + 'ns'))))
def H_55_(O1J7eT202, I_W9Y_V7_):
    return Pair(O1J7eT202, I_W9Y_V7_)

@gQ5Y((('c' + 'a') + chr((142 + -28))))
def YK02q_(O1J7eT202):
    mA79m(O1J7eT202, b4I_37_0C, int(((-0.26317815431300795 + 0.5964010514522479) * int((0.7829642451178267 * 0)))), (('c' + 'a') + chr(114)))
    return O1J7eT202.first

@gQ5Y((('c' + 'd') + chr(114)))
def o4P_HTrE(O1J7eT202):
    mA79m(O1J7eT202, b4I_37_0C, int((((0.21590294058789616 + 0.012193724690551355) + (0.3428725976793532 + 0.04662273133571071)) * int((0.761154257533402 * 0)))), (chr(99) + (str() + ('d' + 'r'))))
    return O1J7eT202.second

@gQ5Y((('s' + ('' + 'et')) + ('-' + ('car' + '!'))))
def YK02q_(O1J7eT202, I_W9Y_V7_):
    mA79m(O1J7eT202, b4I_37_0C, int(((0.6023263797411758 + 0.298325030393896) * int((0.7799947640614965 * 0)))), (chr((38 + 77)) + (('' + 'et-c') + ('ar' + '!'))))
    O1J7eT202.first = I_W9Y_V7_

@gQ5Y(((str() + ('' + 'set')) + (('-' + 'cdr') + '!')))
def o4P_HTrE(O1J7eT202, I_W9Y_V7_):
    mA79m(O1J7eT202, b4I_37_0C, int(((0.24906105951099033 + 0.6995723408159301) * int((0.7150185705097007 * 0)))), (str() + (str() + ('set-cdr' + '!'))))
    if (not scheme.DOTS_ARE_CONS):
        mA79m(I_W9Y_V7_, l3T9671_, (((123 + 18) + (-40 + -48)) + ((-67 + -82) + (83 + 14))), (('s' + ('e' + 't-')) + (('' + 'cd') + ('r' + '!'))))
    O1J7eT202.second = I_W9Y_V7_

@gQ5Y((('' + ('l' + 'is')) + chr((176 + -60))))
def f898u99T(*D0_9D):
    q1Gj04i = nil
    for uWK066 in reversed(D0_9D):
        q1Gj04i = Pair(uWK066, q1Gj04i)
    return q1Gj04i

@gQ5Y(((('' + 'appe') + 'n') + 'd'))
def MEm3gK35(*D0_9D):
    if (len(D0_9D) == int(((0.014451859370070874 + 0.1532937945937981) * 0))):
        return nil
    q1Gj04i = D0_9D[(- (((68 + -69) + (-31 + 64)) + ((-63 + 22) + (103 + -93))))]
    for K_2TKRT8 in range((len(D0_9D) - (((-108 + -62) + (120 + -38)) + ((159 + 14) + (-15 + -68)))), (- (((25 + -26) + (23 + 62)) + ((-183 + 17) + (48 + 35)))), (- (((-15 + 83) + (22 + -84)) + ((29 + -88) + (-41 + 95))))):
        N6g0t8t = D0_9D[K_2TKRT8]
        if (N6g0t8t is not nil):
            mA79m(N6g0t8t, b4I_37_0C, K_2TKRT8, ('' + (('a' + 'ppe') + ('n' + 'd'))))
            j717y_ = t8_pEK = Pair(N6g0t8t.first, q1Gj04i)
            N6g0t8t = N6g0t8t.second
            while b4I_37_0C(N6g0t8t):
                t8_pEK.second = Pair(N6g0t8t.first, q1Gj04i)
                t8_pEK = t8_pEK.second
                N6g0t8t = N6g0t8t.second
            q1Gj04i = j717y_
    return q1Gj04i

@gQ5Y(((('' + 'st') + chr(114)) + (chr(105) + ('ng' + '?'))))
def iv_aT(O1J7eT202):
    return (isinstance(O1J7eT202, str) and O1J7eT202.startswith('"'))

@gQ5Y(('s' + (('ymb' + 'o') + ('' + 'l?'))))
def L__2d69(O1J7eT202):
    return (isinstance(O1J7eT202, str) and (not iv_aT(O1J7eT202)))

@gQ5Y(((('' + 'var') + ('' + 'iad')) + (('ic-sym' + 'bol') + chr(63))))
def AK_06iaOr(O1J7eT202):
    return isinstance(O1J7eT202, e7__HV8)

@gQ5Y((chr((204 + -94)) + (('' + 'umber') + '?')))
def e4W5_t2_3(O1J7eT202):
    return (isinstance(O1J7eT202, numbers.Real) and (not B3np70_Yq(O1J7eT202)))

@gQ5Y(((chr(105) + ('nt' + 'ege')) + (chr(114) + chr(63))))
def d02S8SH(O1J7eT202):
    return (e4W5_t2_3(O1J7eT202) and (isinstance(O1J7eT202, numbers.Integral) or (int(O1J7eT202) == O1J7eT202)))

def b_f_q_(*D0_9D):
    'H_9Cz7665B3l0_0k7fS4'
    for (K_2TKRT8, N6g0t8t) in enumerate(D0_9D):
        if (not e4W5_t2_3(N6g0t8t)):
            HVg58Yd = ((('o' + 'perand') + (' ' + '{0}')) + ((' ({' + '1}) is') + (' not' + ' a number')))
            raise Y6__(HVg58Yd.format(K_2TKRT8, N6g0t8t))

def D577I_B9k(Y__t, Q3m6_1, D0_9D):
    'n4P8xA09Ns01aw7UYi_j2Vjj'
    b_f_q_(*D0_9D)
    mt_q_ = Q3m6_1
    for to7m1Mu_W in D0_9D:
        mt_q_ = Y__t(mt_q_, to7m1Mu_W)
    if (int(mt_q_) == mt_q_):
        mt_q_ = int(mt_q_)
    return mt_q_

@gQ5Y(chr((-7 + 50)))
def O_AG3_5E0(*D0_9D):
    return D577I_B9k(operator.add, int((0.9019427696533496 * 0)), D0_9D)

@gQ5Y(chr(((-1 + 95) + (-128 + 79))))
def f95_qi(niaKR__20, *D0_9D):
    b_f_q_(niaKR__20, *D0_9D)
    if (len(D0_9D) == int(((0.37797813332160013 + 0.44692165271511053) * int((0.22646051513754129 * 0))))):
        return (- niaKR__20)
    return D577I_B9k(operator.sub, niaKR__20, D0_9D)

@gQ5Y(chr(((-82 + 36) + (0 + 88))))
def ax89(*D0_9D):
    return D577I_B9k(operator.mul, (((-118 + -5) + (151 + -54)) + ((-40 + 5) + (-21 + 83))), D0_9D)

@gQ5Y('/')
def OGa0___DG(niaKR__20, *D0_9D):
    b_f_q_(niaKR__20, *D0_9D)
    try:
        if (len(D0_9D) == int((((-0.2780630464824535 + 0.18068556720998952) + (-0.1950983276794328 + 0.49357613041639814)) * int((0.6525098995615177 * 0))))):
            return operator.truediv((((106 + 59) + (-44 + -52)) + ((-124 + 28) + (119 + -91))), niaKR__20)
        return D577I_B9k(operator.truediv, niaKR__20, D0_9D)
    except ZeroDivisionError as s_1_:
        raise Y6__(s_1_)

@gQ5Y((str() + ('e' + ('x' + 'pt'))))
def i5KKo4x(niaKR__20, q94Q4_2i):
    b_f_q_(niaKR__20, q94Q4_2i)
    return pow(niaKR__20, q94Q4_2i)

@gQ5Y((str() + (chr(97) + ('' + 'bs'))))
def d3sd72E0(niaKR__20):
    return abs(niaKR__20)

@gQ5Y(((('' + 'qu') + ('ot' + 'i')) + (str() + ('' + 'ent'))))
def E8Ov367f(niaKR__20, q94Q4_2i):
    b_f_q_(niaKR__20, q94Q4_2i)
    try:
        return ((- ((- niaKR__20) // q94Q4_2i)) if ((niaKR__20 < int(((0.4374043805191248 + 0.10122903064971978) * int((0.4897929022926635 * 0))))) ^ (q94Q4_2i < int((((0.006109011385340368 + 0.0895503590543334) + (0.5411323779709998 + 0.27734342939015155)) * int((0.30351656326284326 * 0)))))) else (niaKR__20 // q94Q4_2i))
    except ZeroDivisionError as s_1_:
        raise Y6__(s_1_)

@gQ5Y(((('' + 'mo') + ('d' + 'u')) + (str() + ('l' + 'o'))))
def UfS_5(niaKR__20, q94Q4_2i):
    b_f_q_(niaKR__20, q94Q4_2i)
    try:
        return (niaKR__20 % q94Q4_2i)
    except ZeroDivisionError as s_1_:
        raise Y6__(s_1_)

@gQ5Y((('' + ('re' + 'm')) + (('ai' + 'nde') + 'r')))
def s01_o_(niaKR__20, q94Q4_2i):
    b_f_q_(niaKR__20, q94Q4_2i)
    try:
        q1Gj04i = (niaKR__20 % q94Q4_2i)
    except ZeroDivisionError as s_1_:
        raise Y6__(s_1_)
    while (((q1Gj04i < int(((0.37802353278098855 + 0.4847193802770373) * int((0.7307342357845545 * 0))))) and (niaKR__20 > int(((-0.02530385278030045 + 0.1702427455077935) * int((0.01096476623294207 * 0)))))) or ((q1Gj04i > int((((-1.2038062406262897 + 0.6679071303452789) + (0.5774151364571258 + 0.060385437678155185)) * 0))) and (niaKR__20 < 0))):
        q1Gj04i -= q94Q4_2i
    return q1Gj04i

def k49734y_(MMs0it63k, V_6_, H3_1M4_=None):
    'v_5B7_B32d4z_8__2A_24_0V07'
    cpw3Gs = (getattr(MMs0it63k, V_6_) if (H3_1M4_ is None) else getattr(MMs0it63k, V_6_, H3_1M4_))

    def i0T1En644(*D0_9D):
        b_f_q_(*D0_9D)
        return cpw3Gs(*D0_9D)
    return i0T1En644
for N0LY_ in [((('' + 'ac') + 'o') + chr((28 + 87))), (chr((90 + 7)) + (('c' + 'o') + ('' + 'sh'))), (chr((140 + -43)) + (('' + 'si') + 'n')), (('a' + chr(115)) + ('i' + ('n' + 'h'))), ((str() + ('' + 'at')) + ('a' + chr(110))), ((chr(97) + 't') + (str() + ('a' + 'n2'))), ('' + ('' + ('' + 'atanh'))), ((chr(99) + 'e') + (chr(105) + chr(108))), (('c' + ('o' + 'p')) + ('' + ('ysi' + 'gn'))), ('' + (chr(99) + ('' + 'os'))), ('c' + (str() + ('' + 'osh'))), ((chr(100) + 'e') + (('' + 'gr') + ('e' + 'es'))), (chr((91 + 11)) + (('l' + 'o') + ('' + 'or'))), (str() + ('l' + ('' + 'og'))), (('l' + ('o' + 'g1')) + '0'), ((chr(108) + chr(111)) + (str() + ('g1' + 'p'))), ((chr(114) + ('ad' + 'ian')) + chr(115)), ('s' + ('i' + 'n')), (chr((143 + -28)) + (('' + 'in') + chr(104))), (str() + (('sq' + 'r') + 't')), (str() + ('' + ('t' + 'an'))), ('t' + (chr(97) + ('n' + 'h'))), (('' + ('' + 'tr')) + (('' + 'un') + 'c'))]:
    gQ5Y(N0LY_)(k49734y_(math, N0LY_))
gQ5Y((('' + ('' + 'log')) + chr(50)))(k49734y_(math, ((str() + ('l' + 'o')) + ('g' + chr(50))), (lambda O1J7eT202: math.log(O1J7eT202, (((111 + -97) + (128 + -57)) + ((-31 + -68) + (-17 + 33)))))))

def k7h21F8(tm_3L6P_1, O1J7eT202, I_W9Y_V7_):
    b_f_q_(O1J7eT202, I_W9Y_V7_)
    return tm_3L6P_1(O1J7eT202, I_W9Y_V7_)

@gQ5Y(chr((7 + 54)))
def fkS4(O1J7eT202, I_W9Y_V7_):
    return k7h21F8(operator.eq, O1J7eT202, I_W9Y_V7_)

@gQ5Y(chr((116 + -56)))
def S82T(O1J7eT202, I_W9Y_V7_):
    return k7h21F8(operator.lt, O1J7eT202, I_W9Y_V7_)

@gQ5Y(chr(((51 + -18) + (-66 + 95))))
def kK5u0_M(O1J7eT202, I_W9Y_V7_):
    return k7h21F8(operator.gt, O1J7eT202, I_W9Y_V7_)

@gQ5Y((str() + (chr(60) + chr(61))))
def Q799wUe8(O1J7eT202, I_W9Y_V7_):
    return k7h21F8(operator.le, O1J7eT202, I_W9Y_V7_)

@gQ5Y((chr((132 + -70)) + chr(61)))
def nWINjMi7(O1J7eT202, I_W9Y_V7_):
    return k7h21F8(operator.ge, O1J7eT202, I_W9Y_V7_)

@gQ5Y((chr((100 + 1)) + (('' + 've') + ('n' + '?'))))
def S1eb(O1J7eT202):
    b_f_q_(O1J7eT202)
    return ((O1J7eT202 % (((39 + 7) + (-15 + 36)) + ((-201 + 90) + (-51 + 97)))) == int((((-0.5753144207495927 + 0.481234637768424) + (0.8761714777098872 + 0.10387658155663249)) * int((0.32560810778216154 * 0)))))

@gQ5Y((('' + ('' + 'od')) + (chr(100) + '?')))
def Y_ZmM419(O1J7eT202):
    b_f_q_(O1J7eT202)
    return ((O1J7eT202 % (((16 + 52) + (-117 + 47)) + ((16 + -2) + (-57 + 47)))) == (((35 + 94) + (-78 + 40)) + ((-100 + -3) + (113 + -100))))

@gQ5Y((chr(122) + (('e' + 'ro') + '?')))
def d6_034Y(O1J7eT202):
    b_f_q_(O1J7eT202)
    return (O1J7eT202 == int(((-0.15293639726879915 + 0.6638334285611124) * int((0.5325054511657719 * 0)))))

@gQ5Y(((('a' + 't') + ('o' + 'm')) + chr((4 + 59))))
def YN1j92F_(O1J7eT202):
    return (B3np70_Yq(O1J7eT202) or e4W5_t2_3(O1J7eT202) or L__2d69(O1J7eT202) or r_l4(O1J7eT202) or iv_aT(O1J7eT202))

@gQ5Y(((('' + 'dis') + chr(112)) + (chr(108) + ('a' + 'y'))))
def iV_5zB(to7m1Mu_W):
    if iv_aT(to7m1Mu_W):
        to7m1Mu_W = eval(to7m1Mu_W)
    print(repl_str(to7m1Mu_W), end=str())

@gQ5Y((('' + ('p' + 'rin')) + chr((190 + -74))))
def c8_1D(to7m1Mu_W):
    print(repl_str(to7m1Mu_W))

@gQ5Y(((chr(110) + 'e') + (('' + 'wlin') + chr(101))))
def Ng0xd70():
    print()
    sys.stdout.flush()

@gQ5Y(((str() + ('' + 'er')) + (('r' + 'o') + 'r')))
def g9_vX29_(HVg58Yd=None):
    HVg58Yd = (str() if (HVg58Yd is None) else repl_str(HVg58Yd))
    raise Y6__(HVg58Yd)

@gQ5Y((str() + (('' + 'ex') + ('i' + 't'))))
def S4fCN614_():
    raise EOFError
'HbXjM8v_w44F_gRN5Nsk_80x_gx__'
tOOwp5pnq = False
i354 = True

def XBZ0aI0():
    return tOOwp5pnq

def M288_O():
    global tOOwp5pnq
    if (not tOOwp5pnq):
        tOOwp5pnq = True
        turtle.title(((str() + ('S' + 'che')) + (('m' + 'e Tu') + ('' + 'rtles'))))
        turtle.mode(('l' + (chr(111) + ('' + 'go'))))

@gQ5Y(((('f' + 'or') + ('w' + 'ar')) + 'd'), (str() + ('' + ('' + 'fd'))))
def t37kIEL(AE7F):
    'JgJ918_bF0791EEzX9N1_zf60'
    b_f_q_(AE7F)
    M288_O()
    turtle.forward(AE7F)

@gQ5Y((chr((159 + -61)) + ('' + ('a' + 'ckward'))), (('' + ('b' + 'a')) + ('' + ('' + 'ck'))), (str() + (str() + ('b' + 'k'))))
def mm88vm1__(AE7F):
    'RH_89e_9E37A3_s5_ACM'
    b_f_q_(AE7F)
    M288_O()
    turtle.backward(AE7F)

@gQ5Y((('' + ('l' + 'e')) + (chr(102) + 't')), (str() + ('' + ('l' + 't'))))
def pWB14(AE7F):
    'o0R2__HDG2_Xz74j5A9xX69B43R5'
    b_f_q_(AE7F)
    M288_O()
    turtle.left(AE7F)

@gQ5Y((str() + ('' + ('ri' + 'ght'))), (str() + ('r' + 't')))
def V57IH5(AE7F):
    'W_hHtt_1n3j2e9SJg34PX9Eb'
    b_f_q_(AE7F)
    M288_O()
    turtle.right(AE7F)

@gQ5Y(((('' + 'ci') + ('' + 'rc')) + ('l' + 'e')))
def m_V81(j717y_, xu2k_t2=None):
    'Es__18m_6j7Z6__32XbqH'
    if (xu2k_t2 is None):
        b_f_q_(j717y_)
    else:
        b_f_q_(j717y_, xu2k_t2)
    M288_O()
    turtle.circle(j717y_, (xu2k_t2 and xu2k_t2))

@gQ5Y(((str() + ('' + 'setpo')) + (chr(115) + ('it' + 'ion'))), (('' + ('s' + 'e')) + (chr(116) + ('po' + 's'))), (chr((43 + 60)) + (chr(111) + ('' + 'to'))))
def BBASg2(O1J7eT202, I_W9Y_V7_):
    'c2_736_Xf7ekjP6Rlm3_yLSy5L6'
    b_f_q_(O1J7eT202, I_W9Y_V7_)
    M288_O()
    turtle.setposition(O1J7eT202, I_W9Y_V7_)

@gQ5Y(((('s' + 'e') + ('' + 'thead')) + (str() + ('i' + 'ng'))), (str() + ('' + ('' + 'seth'))))
def zz6Nj7(IS0a0tuM):
    'u2h_6_997Kp_7a74A8Z48O5'
    b_f_q_(IS0a0tuM)
    M288_O()
    turtle.setheading(IS0a0tuM)

@gQ5Y((chr((199 + -87)) + ('' + ('e' + 'nup'))), (chr(112) + chr(117)))
def Rd1___78W():
    'x9_i_v_8__1Am9zg3_85K_h7_'
    M288_O()
    turtle.penup()

@gQ5Y(((('' + 'pe') + ('' + 'nd')) + (chr(111) + ('' + 'wn'))), (str() + (str() + ('' + 'pd'))))
def K1Z_():
    'O_tn_0FzHo90145R__3G5Rr'
    M288_O()
    turtle.pendown()

@gQ5Y((str() + (('s' + 'h') + ('o' + 'wturtle'))), (str() + ('' + ('s' + 't'))))
def QAD_():
    'Y_91eR4_qk0i208NPt__sUU25V_1'
    M288_O()
    turtle.showturtle()

@gQ5Y((('' + ('h' + 'idetu')) + (('r' + 't') + ('l' + 'e'))), (chr((188 + -84)) + chr(116)))
def C074_():
    'pR__8g_wCK7D40_P5C4_2691'
    M288_O()
    turtle.hideturtle()

@gQ5Y((chr((173 + -74)) + (('le' + 'a') + 'r')))
def nq_suO69():
    'p7oW0q96j3K6_LUP6NF80z'
    M288_O()
    turtle.clear()

@gQ5Y((chr((98 + 1)) + ('' + ('' + 'olor'))))
def u51_9(R_p__N9):
    'mvuqpY9em0j306v9182_50_'
    M288_O()
    mA79m(R_p__N9, iv_aT, int((((-0.40269823948294514 + 0.9124211259587609) + (-0.5027967688759137 + 0.951216607826192)) * int(((-0.08060121890480598 + 0.6403174499444892) * 0)))), (('' + ('c' + 'o')) + (('' + 'lo') + 'r')))
    turtle.color(eval(R_p__N9))

@gQ5Y((chr((100 + 14)) + ('g' + 'b')))
def JgWy(b07Pg5ogg, Sw53C1_03, M2i11500):
    'S636k43rC_YYUf_G__q7Kh8q'
    p_4Mn_Q2 = (b07Pg5ogg, Sw53C1_03, M2i11500)
    for O1J7eT202 in p_4Mn_Q2:
        if ((O1J7eT202 < int(((-0.44371959526306926 + 0.883582493867712) * int((0.8974473202753893 * 0))))) or (O1J7eT202 > (((-76 + -58) + (144 + -48)) + ((175 + -39) + (-108 + 11))))):
            raise Y6__((((('' + 'Illegal color') + ('' + ' i')) + (('nt' + 'e') + ('ns' + 'ity in '))) + repl_str(p_4Mn_Q2)))
    JI_rY = tuple((int((O1J7eT202 * (((292 + 42) + (-132 + 37)) + ((72 + 36) + (-176 + 84))))) for O1J7eT202 in p_4Mn_Q2))
    return (((('"' + '#%0') + ('2' + 'x%02')) + (chr(120) + ('%0' + '2x"'))) % JI_rY)

@gQ5Y((chr((96 + 2)) + (('e' + 'gin_') + ('fil' + 'l'))))
def B08J():
    'D_PeLI_j4_4_8vr07_28f'
    M288_O()
    turtle.begin_fill()

@gQ5Y(((str() + ('' + 'en')) + (('d_' + 'f') + ('' + 'ill'))))
def Fmt_Q_():
    'oBV7Z2_D22_Y2mWlS34Z837'
    M288_O()
    turtle.end_fill()

@gQ5Y(((str() + ('bg' + 'c')) + (('ol' + 'o') + 'r')))
def Hn2n2uX6A(R_p__N9):
    M288_O()
    mA79m(R_p__N9, iv_aT, 0, (str() + (('bg' + 'co') + ('' + 'lor'))))
    turtle.bgcolor(eval(R_p__N9))

@gQ5Y(((str() + ('exi' + 't')) + (chr(111) + ('' + 'nclick'))))
def O_8183():
    'B7G8Gk_58hQpa_H31Iag'
    global tOOwp5pnq
    if (i354 and tOOwp5pnq):
        print(((('Close or click' + ' on turtle window to comple') + chr(116)) + (chr(101) + (' ex' + 'it'))))
        turtle.exitonclick()
        tOOwp5pnq = False

@gQ5Y(((str() + ('s' + 'p')) + ('' + ('' + 'eed'))))
def M21m(mt_q_):
    'WUq2730b2cU1Zn8_5_E9GY7'
    mA79m(mt_q_, d02S8SH, int((((-0.18051527611497198 + 0.4203798396461391) + (-0.540069789025946 + 0.9875239573513356)) * int((0.9665691924516944 * 0)))), ('s' + (('' + 'pe') + ('' + 'ed'))))
    M288_O()
    turtle.speed(mt_q_)

@gQ5Y((str() + ('p' + ('ixe' + 'l'))))
def k__UK(O1J7eT202, I_W9Y_V7_, R_p__N9):
    'bBLR4_8_qT7_b9Ju_7A4x58497_'
    mA79m(R_p__N9, iv_aT, int((((-1.108961204921925 + 0.6553993552022018) + (0.49181020886258375 + 0.17687430262202364)) * int(((0.556411987166369 + 0.1096376863188111) * 0)))), ((('' + 'pi') + chr(120)) + (str() + ('' + 'el'))))
    ha5c5404 = eval(R_p__N9)
    h02_D = turtle.getcanvas()
    (hE72, IS0a0tuM) = (h02_D.winfo_width(), h02_D.winfo_height())
    if (not hasattr(k__UK, (('' + ('ima' + 'g')) + 'e'))):
        M288_O()
        k__UK.image = tkinter.PhotoImage(width=hE72, height=IS0a0tuM)
        h02_D.create_image((int((((-1.0365536137521796 + 0.4001464701459212) + (0.7660865445942473 + 0.03979735030862108)) * int(((0.02958761455852965 + 0.835551654778551) * 0)))), int(((0.3317235787432179 + 0.524737719489253) * 0))), image=k__UK.image, state=((chr(110) + chr(111)) + (('r' + 'ma') + 'l')))
    dkDz_D = k__UK.dkDz_D
    for wj_7Bb_ in range(dkDz_D):
        for K3_X20P9 in range(dkDz_D):
            (SMR1_M3_, tQW_6) = (((O1J7eT202 * dkDz_D) + wj_7Bb_), (IS0a0tuM - ((I_W9Y_V7_ * dkDz_D) + K3_X20P9)))
            if ((0 < SMR1_M3_ < hE72) and (int((((-0.7918253255041632 + 0.835858717595727) + (-0.12757199937859054 + 0.7107951838785683)) * int(((0.11068047111031776 + 0.5348629831662969) * int((0.5167355209054884 * 0)))))) < tQW_6 < IS0a0tuM)):
                k__UK.image.put(ha5c5404, (SMR1_M3_, tQW_6))
k__UK.dkDz_D = (((38 + -21) + (29 + -100)) + ((48 + 88) + (-6 + -75)))

@gQ5Y((('' + ('p' + 'ixels')) + (chr(105) + ('z' + 'e'))))
def V7M4LyBHY(dkDz_D):
    'oR_W9J97k7nB8_160wZEM8'
    b_f_q_(dkDz_D)
    if ((dkDz_D <= int((0.9932891158526612 * 0))) or (not isinstance(dkDz_D, numbers.Integral))):
        raise Y6__((((('Inv' + 'alid pi') + ('' + 'xel ')) + (('s' + 'i') + ('ze:' + ' '))) + repl_str(dkDz_D)))
    k__UK.dkDz_D = dkDz_D

@gQ5Y(((str() + ('' + 'scre')) + (('' + 'en') + ('_' + 'width'))))
def zOQ__mq():
    'v3CAbY8qE_o8a_OV_4Z8Y_gO'
    return (turtle.getcanvas().winfo_width() // k__UK.dkDz_D)

@gQ5Y(((('' + 'sc') + ('ree' + 'n')) + ('_' + ('he' + 'ight'))))
def U_T1_Dm_():
    'tOPL6my6S_M4d73t705sw86xCI__X'
    return (turtle.getcanvas().winfo_height() // k__UK.dkDz_D)
'Hu26Z539k9mOc_Lm637_C_'
m7lNr6LT = (set(string.digits) | set((('+' + '-') + chr((-12 + 58)))))
R__3m = (((set(((('' + '!$%') + ('' + '&*')) + (('/' + ':<=>?@') + ('^_' + '~')))) | set(string.ascii_lowercase)) | set(string.ascii_uppercase)) | m7lNr6LT)
h27_2k_ = set(chr((-14 + 48)))
E07B3F_L = set((' ' + (chr(9) + ('\n' + '\r'))))
Zz_k = set(((str() + ('' + '()[]')) + ("'" + chr(96))))
R5qg4Cr1p = (((E07B3F_L | Zz_k) | h27_2k_) | {chr((84 + -40)), (',' + chr(64))})
GF49L = (Zz_k | {chr((28 + 18)), chr(((-47 + 23) + (88 + -20))), (chr((-23 + 67)) + chr((23 + 41)))})

def nl6h0A(mt_q_):
    'R6_ior7__I__Z3A_qZ01GtA'
    if (len(mt_q_) == int(((0.6514045015020329 + 0.3224466937932743) * 0))):
        return False
    for R_p__N9 in mt_q_:
        if (R_p__N9 not in R__3m):
            return False
    return True

def V8jdyAH__(aYu_, c6O_1MTVr):
    'pKXJ199i2R7a1UK8__1i8Q3'
    while (c6O_1MTVr < len(aYu_)):
        R_p__N9 = aYu_[c6O_1MTVr]
        if (R_p__N9 == chr((150 + -91))):
            return (None, len(aYu_))
        elif (R_p__N9 in E07B3F_L):
            c6O_1MTVr += (((-111 + 18) + (93 + -39)) + ((106 + 30) + (-108 + 12)))
        elif (R_p__N9 in Zz_k):
            if (R_p__N9 == chr(93)):
                R_p__N9 = chr(((62 + 76) + (-126 + 29)))
            if (R_p__N9 == chr(((225 + -44) + (-119 + 29)))):
                R_p__N9 = '('
            return (R_p__N9, (c6O_1MTVr + (((-19 + -97) + (-6 + 71)) + ((67 + -41) + (-10 + 36)))))
        elif (R_p__N9 == chr(35)):
            return (aYu_[c6O_1MTVr:(c6O_1MTVr + (((-62 + 47) + (90 + -31)) + ((-163 + 22) + (8 + 91))))], min((c6O_1MTVr + ((0 + (82 + 9)) + ((-15 + -85) + (-37 + 48)))), len(aYu_)))
        elif (R_p__N9 == chr(((65 + -47) + (114 + -88)))):
            if (((c6O_1MTVr + (((12 + 78) + (11 + -7)) + ((-126 + 54) + (36 + -57)))) < len(aYu_)) and (aYu_[(c6O_1MTVr + (((-143 + 100) + (25 + -34)) + ((-87 + 88) + (-23 + 75))))] == chr((-21 + 85)))):
                return ((',' + chr((119 + -55))), (c6O_1MTVr + ((0 + (-163 + 93)) + ((155 + -71) + (-94 + 82)))))
            return (R_p__N9, (c6O_1MTVr + (((4 + 68) + (-45 + 37)) + ((21 + -83) + (-92 + 91)))))
        elif (R_p__N9 in h27_2k_):
            if (((c6O_1MTVr + (((-47 + 77) + (-51 + 65)) + ((11 + 40) + (-64 + -30)))) < len(aYu_)) and (aYu_[(c6O_1MTVr + (((-141 + 17) + (157 + -97)) + ((70 + 89) + (-119 + 25))))] == R_p__N9)):
                return ((R_p__N9 + R_p__N9), (c6O_1MTVr + (((-99 + 28) + (-85 + 63)) + ((75 + 14) + (60 + -54)))))
            S8N2_ = (bytes(aYu_[c6O_1MTVr:], encoding=(chr((38 + 79)) + (('t' + 'f') + ('-' + '8')))),)
            pN_O65Slt = tokenize.tokenize(iter(S8N2_).__next__)
            next(pN_O65Slt)
            G23_9 = next(pN_O65Slt)
            if (G23_9.type != tokenize.STRING):
                raise ValueError(((('' + 'inva') + ('l' + 'id string')) + (('' + ': ') + ('{0' + '}'))).format(G23_9.string))
            return (G23_9.string, (G23_9.end[(((-88 + -11) + (7 + 46)) + ((86 + -85) + (140 + -94)))] + c6O_1MTVr))
        else:
            q_9l = c6O_1MTVr
            while ((q_9l < len(aYu_)) and (aYu_[q_9l] not in R5qg4Cr1p)):
                q_9l += (((-49 + 57) + (-101 + 4)) + ((131 + -79) + (67 + -29)))
            return (aYu_[c6O_1MTVr:q_9l], min(q_9l, len(aYu_)))
    return (None, len(aYu_))

def X76v(aYu_):
    'e12q_175__131s8Y_3_t_j_6'
    q1Gj04i = []
    (P11713X5h, K_2TKRT8) = V8jdyAH__(aYu_, int((((-0.5390240001134124 + 0.8240387803198138) + (-0.19078522127202435 + 0.8979715849459257)) * int(((0.2739342036169151 + 0.14530009366070307) * int((0.5843965952875967 * 0)))))))
    while (P11713X5h is not None):
        if (P11713X5h in GF49L):
            q1Gj04i.append(P11713X5h)
        elif ((P11713X5h == (chr((-12 + 47)) + chr((136 + -20)))) or (P11713X5h.lower() == (chr((103 + 13)) + (('' + 'ru') + chr(101))))):
            q1Gj04i.append(True)
        elif ((P11713X5h == ('' + ('' + ('' + '#f')))) or (P11713X5h.lower() == ('' + (('f' + 'al') + ('s' + 'e'))))):
            q1Gj04i.append(False)
        elif (P11713X5h == (str() + (chr(110) + ('i' + 'l')))):
            q1Gj04i.append(P11713X5h)
        elif (P11713X5h[int((0.9522661423582656 * 0))] in R__3m):
            B_5_7W = False
            if (P11713X5h[int((((-0.6313141375472378 + 0.06496815355047736) + (-0.2672616692624634 + 0.9574822231742746)) * 0))] in m7lNr6LT):
                try:
                    q1Gj04i.append(int(P11713X5h))
                    B_5_7W = True
                except ValueError:
                    try:
                        q1Gj04i.append(float(P11713X5h))
                        B_5_7W = True
                    except ValueError:
                        pass
            if (not B_5_7W):
                if nl6h0A(P11713X5h):
                    q1Gj04i.append(P11713X5h.lower())
                else:
                    raise ValueError(((('' + 'inval') + ('' + 'id numer')) + (('al or symbol' + ': {') + ('0' + '}'))).format(P11713X5h))
        elif (P11713X5h[int((((-0.40358036921654084 + 0.3425816907990118) + (-0.22751213913052792 + 0.3722629152419594)) * 0))] in h27_2k_):
            q1Gj04i.append(P11713X5h)
        else:
            print(((chr(119) + ('a' + 'rni')) + (('ng: ' + 'in') + ('valid token: ' + '{0}'))).format(P11713X5h), file=sys.stderr)
            print(('' + (' ' + ('  ' + ' '))), aYu_, file=sys.stderr)
            print((chr((39 + -7)) * (K_2TKRT8 + (((-22 + -90) + (133 + -92)) + ((-72 + 67) + (147 + -68))))), chr((142 + -48)), file=sys.stderr)
        (P11713X5h, K_2TKRT8) = V8jdyAH__(aYu_, K_2TKRT8)
    return q1Gj04i

def g8_Oo(input):
    'n_8Y8967ae6_87_Ic9MV8'
    return (X76v(aYu_) for aYu_ in input)

def NZU2642(input):
    'c0_E8JvX7gi4282N93_3y'
    return len(list(itertools.chain(*g8_Oo(input))))

def O_Yu(*xP7_9BaX):
    import argparse
    f_XTp = argparse.ArgumentParser(description=(chr((75 + -8)) + (chr(111) + ('unt Scheme ' + 'tokens.'))))
    f_XTp.add_argument((('' + ('f' + 'i')) + (str() + ('' + 'le'))), nargs=chr(((112 + 29) + (-34 + -44))), type=argparse.FileType(chr(((151 + -76) + (-53 + 92)))), default=sys.stdin, help=(('i' + 'n') + (('put file to ' + 'be coun') + ('' + 'ted'))))
    xP7_9BaX = f_XTp.parse_args()
    print(('c' + ('o' + ('unte' + 'd'))), NZU2642(xP7_9BaX.file), (chr((175 + -59)) + (('oke' + 'n') + chr(115))))
'L34jd2_wSEqV5199Ysug'
__version__ = (str() + (chr(49) + ('' + '.2.4')))
globals()[((chr(68) + chr(79)) + (('' + 'TS') + ('_ARE_' + 'CONS')))] = False

def o_Mv_g08D(D8Ec4_01, IU4__, g8_c06K=None):
    'E4AT508r193e_3U01tzq_6X4_'
    IU4__.stack.append(D8Ec4_01)
    if L__2d69(D8Ec4_01):
        q1Gj04i = IU4__.q_F_c4208(D8Ec4_01)
        IU4__.stack.pop()
        return q1Gj04i
    elif AK_06iaOr(D8Ec4_01):
        raise Y6__((chr((90 + -23)) + (('' + 'ann') + ('ot eva' + 'luate variadic symbol'))))
    elif mow4478_9(D8Ec4_01):
        IU4__.stack.pop()
        return D8Ec4_01
    if (not SjS5gc8(D8Ec4_01)):
        raise Y6__(((('m' + 'alf') + ('ormed' + ' ')) + (('list' + ':') + (' {0' + '}'))).format(repl_str(D8Ec4_01)))
    (first, b_fb7) = (D8Ec4_01.first, D8Ec4_01.second)
    if (L__2d69(first) and (first in a2_08p0_0)):
        q1Gj04i = a2_08p0_0[first](b_fb7, IU4__)
        IU4__.stack.pop()
        return q1Gj04i
    else:
        V_J931iS = o_Mv_g08D(first, IU4__)
        T63hC0_(V_J931iS)
        if isinstance(V_J931iS, H3pGJGl):
            D8Ec4_01 = V_J931iS.y_u__6(b_fb7, IU4__)
            q1Gj04i = o_Mv_g08D(D8Ec4_01, IU4__)
        else:
            xP7_9BaX = b_fb7.map((lambda c5Z_: o_Mv_g08D(c5Z_, IU4__)))
            q1Gj04i = RCRH9I__(V_J931iS, xP7_9BaX, IU4__)
        IU4__.stack.pop()
        return q1Gj04i

def mow4478_9(D8Ec4_01):
    'v5_0_55JM0Av7_86U_Pk_'
    return ((YN1j92F_(D8Ec4_01) and (not L__2d69(D8Ec4_01))) or (D8Ec4_01 is None))

def RCRH9I__(V_J931iS, xP7_9BaX, IU4__):
    'v2_48_3JE_9355m77d1k0I5'
    T63hC0_(V_J931iS)
    if isinstance(V_J931iS, BuiltinProcedure):
        return V_J931iS.Ms_5or9(xP7_9BaX, IU4__)
    else:
        a97__ = V_J931iS.qdhGA5_(xP7_9BaX, IU4__)
        return D074_WDB(V_J931iS.X9N4f, a97__)

def D074_WDB(x8Ynq53_, IU4__):
    'JnCM01_J_2hh2D__m4053_U3jr'
    kZ9O91gZy = None
    while (x8Ynq53_ is not nil):
        Ha9x_nVD = (x8Ynq53_.second is nil)
        kZ9O91gZy = o_Mv_g08D(x8Ynq53_.first, IU4__, Ha9x_nVD)
        x8Ynq53_ = x8Ynq53_.second
    return kZ9O91gZy

class c_XsKfu4u(object):
    'AG_UtZC3xp6__h1g1_0BCl'

    def __init__(OnB2B__, j_zpjd24H):
        'fl435_U1_9sm9B_5LmO58_'
        OnB2B__.X__eDK9N = {
            
        }
        OnB2B__.j_zpjd24H = j_zpjd24H
        if OnB2B__.j_zpjd24H:
            OnB2B__.stack = OnB2B__.j_zpjd24H.stack
        else:
            OnB2B__.stack = []

    def __repr__(OnB2B__):
        if (OnB2B__.j_zpjd24H is None):
            return ('' + (('<Global Fram' + 'e') + chr(62)))
        mt_q_ = sorted([((('' + '{0}:') + (' ' + '{')) + ('' + ('' + '1}'))).format(c6O_1MTVr, N6g0t8t) for (c6O_1MTVr, N6g0t8t) in OnB2B__.X__eDK9N.items()])
        return ((('' + '<{') + ('' + '{{0')) + (('' + '}}} -> {') + ('' + '1}>'))).format((str() + ('' + (',' + ' '))).join(mt_q_), repr(OnB2B__.j_zpjd24H))

    def yJ3M06_(OnB2B__, Ibi_X7P, kZ9O91gZy):
        'i1_4V_ZUg_130dM_Z8u84_M_b__9'
        OnB2B__.X__eDK9N[Ibi_X7P] = kZ9O91gZy

    def q_F_c4208(OnB2B__, Ibi_X7P):
        'Q57_66q07g16T14uqv2K_4'
        uWK066 = OnB2B__
        while (uWK066 is not None):
            if (Ibi_X7P in uWK066.X__eDK9N):
                return uWK066.X__eDK9N[Ibi_X7P]
            uWK066 = uWK066.j_zpjd24H
        raise Y6__(((('' + 'unkn') + ('own id' + 'ent')) + (('if' + 'i') + ('' + 'er: {0}'))).format(Ibi_X7P))

    def Oyy2(OnB2B__, Ibi_X7P, kZ9O91gZy):
        'n_3j_dbyd0B8s03U_9_8_5vY_0'
        uWK066 = OnB2B__
        while (uWK066 is not None):
            if (Ibi_X7P in uWK066.X__eDK9N):
                uWK066.X__eDK9N[Ibi_X7P] = kZ9O91gZy
                return
            uWK066 = uWK066.j_zpjd24H
        raise Y6__(((('u' + 'nkno') + ('' + 'wn id')) + (chr(101) + ('ntifier: {' + '0}'))).format(Ibi_X7P))

    def b_73A11I8(OnB2B__, x38695s, D0_9D):
        'cOr011936_9p16y0W_165'
        wCH_E = c_XsKfu4u(OnB2B__)
        while isinstance(x38695s, Pair):
            if AK_06iaOr(x38695s.first):
                assert (x38695s.second is nil), ((('should h' + 'ave') + chr(32)) + (('' + 'be') + ('en caught earlie' + 'r')))
                wCH_E.yJ3M06_(x38695s.first.Ibi_X7P, D0_9D)
                return wCH_E
            if (D0_9D is nil):
                raise Y6__(((('t' + 'oo') + (' few a' + 'rgumen')) + (('ts to funct' + 'ion ') + ('c' + 'all'))))
            wCH_E.yJ3M06_(x38695s.first, D0_9D.first)
            (x38695s, D0_9D) = (x38695s.second, D0_9D.second)
        if (x38695s != nil):
            wCH_E.yJ3M06_(x38695s, D0_9D)
        elif (D0_9D != nil):
            raise Y6__((('t' + 'o') + (('o' + ' ma') + ('ny argumen' + 'ts to function call'))))
        return wCH_E

class p67Nj(object):
    'C6_x3dj_57V2l_Vf0_l51Y627'

def tjf7_65Al(O1J7eT202):
    return isinstance(O1J7eT202, p67Nj)

class BuiltinProcedure(p67Nj):
    'FALW0oB1_atP_F6ZGSPU'

    def __init__(OnB2B__, Y__t, t257wH=False, V_6_='builtin'):
        OnB2B__.V_6_ = V_6_
        OnB2B__.Y__t = Y__t
        OnB2B__.t257wH = t257wH

    def __str__(OnB2B__):
        return (str() + (('' + '#[') + ('{0' + '}]'))).format(OnB2B__.V_6_)

    def Ms_5or9(OnB2B__, xP7_9BaX, IU4__):
        'Ii1dh9_i2_2lYCT99mOW2'
        if (not SjS5gc8(xP7_9BaX)):
            raise Y6__(((('ar' + 'gu') + ('m' + 'e')) + (('nts ar' + 'e not in a list: {0') + chr(125))).format(xP7_9BaX))
        MtvAm6j_ = []
        while (xP7_9BaX is not nil):
            MtvAm6j_.append(xP7_9BaX.first)
            xP7_9BaX = xP7_9BaX.second
        if OnB2B__.t257wH:
            MtvAm6j_.append(IU4__)
        try:
            return OnB2B__.Y__t(*MtvAm6j_)
        except TypeError as s_1_:
            raise Y6__(((('incorr' + 'ect number of ') + ('argu' + 'men')) + ('' + ('ts: ' + '{0}'))).format(OnB2B__))

class LambdaProcedure(p67Nj):
    'Irb6639_3_80Y8_oM46_I'
    V_6_ = ((('[' + 'l') + ('a' + 'm')) + (('' + 'bda') + chr(93)))

    def __init__(OnB2B__, x38695s, X9N4f, IU4__):
        'px26a_261HfW0Ts25UO6_v_M15p'
        OnB2B__.x38695s = x38695s
        OnB2B__.X9N4f = X9N4f
        OnB2B__.IU4__ = IU4__

    def qdhGA5_(OnB2B__, xP7_9BaX, IU4__):
        'U3_l36e41k0B__81Bu884_'
        return OnB2B__.IU4__.b_73A11I8(OnB2B__.x38695s, xP7_9BaX)

    def __str__(OnB2B__):
        return str(Pair((chr((110 + -2)) + (('amb' + 'd') + chr(97))), Pair(OnB2B__.x38695s, OnB2B__.X9N4f)))

    def __repr__(OnB2B__):
        return ((('LambdaProc' + 'edure({0}, {1}, ') + ('{' + '2}')) + chr((40 + 1))).format(repr(OnB2B__.x38695s), repr(OnB2B__.X9N4f), repr(OnB2B__.IU4__))

class H3pGJGl(LambdaProcedure):
    'j22Fz_7_7XSfx_k4m0i0_'

    def y_u__6(OnB2B__, Y__1, IU4__):
        'J8t2v5jo633tf69ZDKy_H9_1_7m'
        return E6J4R_(OnB2B__, Y__1, IU4__)

def eN_46__2(c0iZ3_, f07IA):
    'c53M7T_h6v__bcT4wEnN10x_M6n'
    for (V_6_, Y__t, c9_1W4) in f07IA:
        c0iZ3_.yJ3M06_(V_6_, BuiltinProcedure(Y__t, V_6_=c9_1W4))

def XfROn0_2(x8Ynq53_, IU4__):
    'R1L0_7l_sP_93D9_9e8p'
    L_F75il2M(x8Ynq53_, (((-12 + 42) + (-32 + -63)) + ((-10 + 8) + (30 + 39))))
    z__71_4_2 = x8Ynq53_.first
    if L__2d69(z__71_4_2):
        L_F75il2M(x8Ynq53_, (((-14 + 80) + (-72 + 89)) + ((-55 + -20) + (86 + -92))), (((135 + 5) + (-24 + -60)) + ((-78 + 98) + (-31 + -43))))
        kZ9O91gZy = o_Mv_g08D(x8Ynq53_.second.first, IU4__)
        IU4__.yJ3M06_(z__71_4_2, kZ9O91gZy)
        return z__71_4_2
    elif (isinstance(z__71_4_2, Pair) and L__2d69(z__71_4_2.first)):
        V_6_ = z__71_4_2.first
        x38695s = z__71_4_2.second
        X9N4f = x8Ynq53_.second
        kZ9O91gZy = I84_xF98(Pair(x38695s, X9N4f), IU4__)
        kZ9O91gZy.V_6_ = V_6_
        IU4__.yJ3M06_(V_6_, kZ9O91gZy)
        return V_6_
    else:
        C_725X = (z__71_4_2.first if isinstance(z__71_4_2, Pair) else z__71_4_2)
        raise Y6__(((('non' + '-sym') + ('bol:' + ' {0')) + chr((174 + -49))).format(C_725X))

def s8_Vx(x8Ynq53_, IU4__):
    'B0l_5301_6Us2f__R8A5393_V7_'
    L_F75il2M(x8Ynq53_, (((-162 + 78) + (4 + 51)) + ((-151 + 92) + (120 + -31))), (((-157 + 51) + (67 + 28)) + ((-177 + 98) + (3 + 88))))
    return x8Ynq53_.first

def e70_L(x8Ynq53_, IU4__):
    'T_O82oS69_u_P0226E6Lq3U1lrW0_'
    L_F75il2M(x8Ynq53_, (((79 + -8) + (-116 + 34)) + ((136 + -61) + (32 + -95))))
    return D074_WDB(x8Ynq53_, IU4__)

def I84_xF98(x8Ynq53_, IU4__):
    'B90678bW8j7oCCp16_8H_C_8'
    L_F75il2M(x8Ynq53_, (((24 + 75) + (59 + -67)) + ((-129 + -57) + (56 + 41))))
    x38695s = x8Ynq53_.first
    wA3_n2(x38695s)
    return LambdaProcedure(x38695s, x8Ynq53_.second, IU4__)

def tH_zb3__6(x8Ynq53_, IU4__):
    'fdTK57s9F9K5lh624hl_6YV'
    L_F75il2M(x8Ynq53_, (((-71 + -35) + (-65 + 95)) + ((30 + 91) + (-137 + 94))), (((-65 + 20) + (-3 + -49)) + ((28 + -27) + (123 + -24))))
    if SheK6O_6(o_Mv_g08D(x8Ynq53_.first, IU4__)):
        return o_Mv_g08D(x8Ynq53_.second.first, IU4__, True)
    elif (len(x8Ynq53_) == (((125 + -76) + (-143 + 61)) + ((78 + 42) + (-6 + -78)))):
        return o_Mv_g08D(x8Ynq53_.second.second.first, IU4__, True)

def v5__sJa8(x8Ynq53_, IU4__):
    'K828a895DXx5W8__ut32_35_Y26'
    kZ9O91gZy = True
    while (x8Ynq53_ is not nil):
        Ha9x_nVD = (x8Ynq53_.second is nil)
        kZ9O91gZy = o_Mv_g08D(x8Ynq53_.first, IU4__, Ha9x_nVD)
        if wJ98___(kZ9O91gZy):
            return kZ9O91gZy
        x8Ynq53_ = x8Ynq53_.second
    return kZ9O91gZy

def B7QL5N(x8Ynq53_, IU4__):
    'O7c_l__73B_2_3C97APwotO0gG'
    kZ9O91gZy = False
    while (x8Ynq53_ is not nil):
        Ha9x_nVD = (x8Ynq53_.second is nil)
        kZ9O91gZy = o_Mv_g08D(x8Ynq53_.first, IU4__, Ha9x_nVD)
        if SheK6O_6(kZ9O91gZy):
            return kZ9O91gZy
        x8Ynq53_ = x8Ynq53_.second
    return kZ9O91gZy

def O__37_U6(x8Ynq53_, IU4__):
    'l96v3hUIy00Zg_m0C83w1U'
    while (x8Ynq53_ is not nil):
        YglxiK8HA = x8Ynq53_.first
        L_F75il2M(YglxiK8HA, (((-142 + -5) + (-52 + 100)) + ((276 + -91) + (-33 + -52))))
        if (YglxiK8HA.first == ((('' + 'el') + 's') + chr((32 + 69)))):
            X_qdn = True
            if (x8Ynq53_.second != nil):
                raise Y6__(('e' + (('ls' + 'e mu') + ('st ' + 'be last'))))
        else:
            X_qdn = o_Mv_g08D(YglxiK8HA.first, IU4__)
        if SheK6O_6(X_qdn):
            if (len(YglxiK8HA) == (((-27 + 26) + (89 + -68)) + ((-13 + -42) + (93 + -57)))):
                return X_qdn
            else:
                return D074_WDB(YglxiK8HA.second, IU4__)
        x8Ynq53_ = x8Ynq53_.second

def gf62(x8Ynq53_, IU4__):
    'XVt8ch_8__75Z4QH05dL_6_'
    L_F75il2M(x8Ynq53_, (((-90 + 41) + 0) + ((95 + 48) + (-89 + -3))))
    tm_y = Y02q(x8Ynq53_.first, IU4__)
    return D074_WDB(x8Ynq53_.second, tm_y)

def Y02q(X__eDK9N, IU4__):
    'Z_t1H4_65Rr5o8hl33md97U_R8'
    if (not SjS5gc8(X__eDK9N)):
        raise Y6__(((('bad bi' + 'ndings') + (' li' + 'st in let for')) + chr((193 + -84))))
    (I3G__m37, z4__1_) = (nil, nil)
    while (X__eDK9N is not nil):
        FM6T0_ = X__eDK9N.first
        L_F75il2M(FM6T0_, (((-71 + 21) + (-17 + -16)) + ((70 + -26) + (-6 + 47))), (((93 + 67) + (-73 + -25)) + ((72 + -47) + (-133 + 48))))
        V_6_ = FM6T0_.first
        to7m1Mu_W = o_Mv_g08D(FM6T0_.second.first, IU4__)
        I3G__m37 = Pair(V_6_, I3G__m37)
        z4__1_ = Pair(to7m1Mu_W, z4__1_)
        X__eDK9N = X__eDK9N.second
    wA3_n2(I3G__m37)
    return IU4__.b_73A11I8(I3G__m37, z4__1_)

def NJ0_Z9(x8Ynq53_, IU4__):
    'keO95Q8Z7f01X_3_77_C9N0_DCG'
    L_F75il2M(x8Ynq53_, (((-9 + 83) + (-103 + 87)) + ((38 + -30) + (-163 + 99))))
    z__71_4_2 = x8Ynq53_.first
    if (isinstance(z__71_4_2, Pair) and L__2d69(z__71_4_2.first)):
        V_6_ = z__71_4_2.first
        x38695s = z__71_4_2.second
        X9N4f = x8Ynq53_.second
        wA3_n2(x38695s)
        kZ9O91gZy = H3pGJGl(x38695s, X9N4f, IU4__)
        kZ9O91gZy.V_6_ = V_6_
        IU4__.yJ3M06_(V_6_, kZ9O91gZy)
        return V_6_
    else:
        raise Y6__((('i' + ('mproper fo' + 'rm fo')) + (('r' + ' de') + ('' + 'fine-macro'))))

def td860(x8Ynq53_, IU4__):
    'KWg798bf45_T_I42g_BL_S0'

    def r538(to7m1Mu_W, IU4__, EH_I7l_X):
        'KS305zDd30_K1sz__Qo04AF_jH7CA'
        if (not b4I_37_0C(to7m1Mu_W)):
            return to7m1Mu_W
        if (to7m1Mu_W.first == ((chr(117) + ('' + 'nq')) + (('uo' + 't') + chr(101)))):
            EH_I7l_X -= (((-161 + 95) + (96 + -94)) + ((-36 + 88) + (77 + -64)))
            if (EH_I7l_X == int((((-0.8231076717339568 + 0.5167572896301464) + (-0.22986893042821344 + 0.8573272681782428)) * 0))):
                x8Ynq53_ = to7m1Mu_W.second
                L_F75il2M(x8Ynq53_, (((-10 + 51) + (59 + -82)) + ((-17 + -28) + (33 + -5))), (((-11 + -98) + (126 + -77)) + ((-4 + 6) + (87 + -28))))
                return o_Mv_g08D(x8Ynq53_.first, IU4__)
        elif (to7m1Mu_W.first == ((('' + 'qua') + 's') + (('i' + 'quo') + ('t' + 'e')))):
            EH_I7l_X += (((-50 + -54) + (11 + 74)) + ((62 + -18) + (-45 + 21)))
        first = r538(to7m1Mu_W.first, IU4__, EH_I7l_X)
        second = r538(to7m1Mu_W.second, IU4__, EH_I7l_X)
        return Pair(first, second)
    L_F75il2M(x8Ynq53_, (((37 + -4) + (-10 + -80)) + ((-71 + 29) + (200 + -100))), (((3 + 6) + (-25 + 10)) + ((-53 + 27) + (-43 + 76))))
    return r538(x8Ynq53_.first, IU4__, (((-44 + 17) + (-12 + -47)) + ((26 + -37) + (86 + 12))))

def tZ028(x8Ynq53_, IU4__):
    raise Y6__((str() + (('unquo' + 'te outside of qu') + ('as' + 'iquote'))))

def s_yve_(x8Ynq53_, IU4__):
    'wc6T4k7YJ4fHp7N6948_p547h'
    L_F75il2M(x8Ynq53_, (((-113 + 88) + (-46 + 45)) + ((63 + -69) + (21 + 13))))
    V_6_ = x8Ynq53_.first
    if (not L__2d69(V_6_)):
        raise Y6__(((('' + ('b' + 'ad')) + ((' ar' + 'gume') + ('nt' + ': '))) + repl_str(V_6_)))
    kZ9O91gZy = o_Mv_g08D(x8Ynq53_.second.first, IU4__)
    IU4__.Oyy2(V_6_, kZ9O91gZy)

def td860(x8Ynq53_, IU4__):
    'I1K12s_DBnK3_J__P_549hv99_n2e'
    L_F75il2M(x8Ynq53_, (((157 + -35) + (-20 + -71)) + ((0 + -35) + (94 + -89))), (((-27 + 100) + (-81 + 5)) + ((5 + 94) + (-105 + 10))))
    (to7m1Mu_W, vf3LM_) = r538(x8Ynq53_.first, IU4__)
    if vf3LM_:
        HVg58Yd = ((('unquote-spli' + 'c') + ('i' + 'n')) + (('g no' + 't in') + ('' + ' list template: {0}')))
        raise Y6__(HVg58Yd.format(x8Ynq53_.first))
    return to7m1Mu_W

def r538(to7m1Mu_W, IU4__, EH_I7l_X=1):
    'yuq_Ly805b4B__1__g32__2'
    if b4I_37_0C(to7m1Mu_W):
        if (to7m1Mu_W.first in ((chr((169 + -52)) + (('nquo' + 't') + chr(101))), ((str() + ('' + 'un')) + ('q' + ('uote-splici' + 'ng'))))):
            EH_I7l_X -= (((-27 + 40) + (-25 + -45)) + ((-39 + 21) + (0 + 76)))
            if (EH_I7l_X == int((((-0.010850140986784496 + 0.8391608090857643) + (-0.7693265440555812 + 0.8248662928254592)) * int((0.03133187114185054 * 0))))):
                x8Ynq53_ = to7m1Mu_W.second
                L_F75il2M(x8Ynq53_, (((-58 + -7) + (32 + -62)) + ((84 + 46) + (26 + -60))), (((-28 + 75) + (9 + -84)) + ((22 + 18) + (-41 + 30))))
                G05G_ = o_Mv_g08D(x8Ynq53_.first, IU4__)
                vf3LM_ = (to7m1Mu_W.first == ((('u' + 'n') + ('qu' + 'o')) + (('te-sp' + 'lic') + ('in' + 'g'))))
                if (vf3LM_ and (not SjS5gc8(G05G_))):
                    HVg58Yd = (str() + (('unquote-splici' + 'ng used on no') + ('n' + '-list: {0}')))
                    raise Y6__(HVg58Yd.format(G05G_))
                return (G05G_, vf3LM_)
        elif (to7m1Mu_W.first == ((('q' + 'ua') + ('' + 'si')) + (('' + 'quo') + ('' + 'te')))):
            EH_I7l_X += (((-172 + 43) + (130 + -75)) + ((167 + -39) + (-45 + -8)))
        (first, vf3LM_) = r538(to7m1Mu_W.first, IU4__, EH_I7l_X)
        (second, g8_c06K) = r538(to7m1Mu_W.second, IU4__, EH_I7l_X)
        if vf3LM_:
            if (second is not nil):
                return (MEm3gK35(first, second), False)
            return (first, False)
        return (Pair(first, second), False)
    else:
        return (to7m1Mu_W, False)
a2_08p0_0 = {
    (chr((139 + -42)) + ('' + ('n' + 'd'))): v5__sJa8,
    ((chr(98) + chr(101)) + (str() + ('gi' + 'n'))): e70_L,
    (str() + (('' + 'co') + ('' + 'nd'))): O__37_U6,
    ('d' + (('' + 'efi') + ('' + 'ne'))): XfROn0_2,
    ('' + ('' + ('i' + 'f'))): tH_zb3__6,
    (('l' + ('' + 'am')) + (str() + ('bd' + 'a'))): I84_xF98,
    (str() + (('' + 'le') + 't')): gf62,
    (chr((53 + 58)) + chr((140 + -26))): B7QL5N,
    (chr((36 + 77)) + ('' + ('uot' + 'e'))): s8_Vx,
    ((str() + ('defin' + 'e')) + (('-' + 'm') + ('ac' + 'ro'))): NJ0_Z9,
    (('' + ('quas' + 'iqu')) + ('o' + ('' + 'te'))): td860,
    ((str() + ('u' + 'nq')) + (('u' + 'ot') + chr(101))): tZ028,
    (('' + ('s' + 'et')) + '!'): s_yve_,
    (str() + (('un' + 'quo') + ('te' + '-splicing'))): tZ028,
}

def L_F75il2M(D8Ec4_01, min, max=float('inf')):
    'EO16s_1j_2Cr40Y25_n_3L_a60E_c'
    if (not SjS5gc8(D8Ec4_01)):
        raise Y6__((((('badly' + ' ') + ('formed e' + 'xpressio')) + (str() + ('n' + ': '))) + repl_str(D8Ec4_01)))
    kwb9A7z57 = len(D8Ec4_01)
    if (kwb9A7z57 < min):
        raise Y6__(((str() + ('too f' + 'ew ')) + (('' + 'op') + ('eran' + 'ds in form'))))
    elif (kwb9A7z57 > max):
        raise Y6__(((('t' + 'o') + 'o') + ((' many o' + 'peran') + ('ds in fo' + 'rm'))))

def wA3_n2(x38695s):
    'pd1ix77D_p96n8InO_21GZN9'
    m6V_j54_ = set()

    def K7328_(Ibi_X7P, Mdy_J00_):
        if (AK_06iaOr(Ibi_X7P) and Mdy_J00_):
            Ibi_X7P = Ibi_X7P.Ibi_X7P
        if (not L__2d69(Ibi_X7P)):
            raise Y6__(((str() + ('' + 'non-s')) + (('' + 'ymbol: {0') + chr(125))).format(Ibi_X7P))
        if (Ibi_X7P in m6V_j54_):
            raise Y6__(((str() + ('' + 'dup')) + (('licate sy' + 'mb') + ('ol:' + ' {0}'))).format(Ibi_X7P))
        m6V_j54_.add(Ibi_X7P)
    while isinstance(x38695s, Pair):
        K7328_(x38695s.first, (x38695s.second is nil))
        x38695s = x38695s.second
    if (x38695s != nil):
        import scheme
        if scheme.DOTS_ARE_CONS:
            K7328_(x38695s, True)
        else:
            raise Y6__((str() + (('Formals' + ' must be ') + ('a li' + 'st'))))

def T63hC0_(V_J931iS):
    'e_zdvl8V2dzs997j20_9_w2__1'
    if (not tjf7_65Al(V_J931iS)):
        raise Y6__(((('' + '{0') + ('}' + ' is ')) + (('no' + 't c') + ('all' + 'able: {1}'))).format(type(V_J931iS).__name__.lower(), repl_str(V_J931iS)))

class MuProcedure(p67Nj):
    'c538nE686D4Z9T7Adw6s6D2JX95F'
    V_6_ = (str() + (chr(91) + ('' + 'mu]')))

    def __init__(OnB2B__, x38695s, X9N4f):
        'Z0NvK3_dVpCF9ej_5_qz1M1k'
        OnB2B__.x38695s = x38695s
        OnB2B__.X9N4f = X9N4f

    def qdhGA5_(OnB2B__, xP7_9BaX, IU4__):
        'CQ615lf0GJ87vv_5R9S03p_8'
        return IU4__.b_73A11I8(OnB2B__.x38695s, xP7_9BaX)

    def __str__(OnB2B__):
        return str(Pair(('' + ('m' + chr(117))), Pair(OnB2B__.x38695s, OnB2B__.X9N4f)))

    def __repr__(OnB2B__):
        return ((('Mu' + 'P') + ('rocedure' + '(')) + (('{0},' + ' ') + ('{1' + '})'))).format(repr(OnB2B__.x38695s), repr(OnB2B__.X9N4f))

def m1gW2A___(x8Ynq53_, IU4__):
    'JO7_ewks_7115J_G63_C807153iR'
    L_F75il2M(x8Ynq53_, (((-73 + -5) + (61 + 24)) + ((126 + -96) + (-12 + -23))))
    x38695s = x8Ynq53_.first
    wA3_n2(x38695s)
    return MuProcedure(x38695s, x8Ynq53_.second)
a2_08p0_0[(str() + (str() + ('m' + 'u')))] = m1gW2A___

class Promise(object):
    'Xb2rzZ_5me4_f_3jz1XO_w0tuK6g'

    def __init__(OnB2B__, qXk_8l_, IU4__):
        OnB2B__.qXk_8l_ = qXk_8l_
        OnB2B__.IU4__ = IU4__

    def h4r_Rq(OnB2B__):
        if (OnB2B__.qXk_8l_ is not None):
            kZ9O91gZy = o_Mv_g08D(OnB2B__.qXk_8l_, OnB2B__.IU4__.b_73A11I8(nil, nil))
            import scheme
            if ((not scheme.DOTS_ARE_CONS) and (not ((kZ9O91gZy is nil) or isinstance(kZ9O91gZy, Pair)))):
                raise Y6__((((('r' + 'esu') + ('lt' + ' of for')) + (('cing ' + 'a pr') + ('omise ' + 'should be a pair or nil, but was %s'))) % kZ9O91gZy))
            OnB2B__.kZ9O91gZy = kZ9O91gZy
            OnB2B__.qXk_8l_ = None
        return OnB2B__.kZ9O91gZy

    def __str__(OnB2B__):
        return ((('#' + '[pr') + ('omise ' + '(')) + ('' + ('{0}forced' + ')]'))).format(((('' + ('' + 'no')) + ('' + ('' + 't '))) if (OnB2B__.qXk_8l_ is not None) else str()))

def P_s_o(x8Ynq53_, IU4__):
    'Q16W7__wz_2WD9abKw5c5'
    L_F75il2M(x8Ynq53_, (((74 + -30) + (-127 + 28)) + ((109 + -7) + (45 + -91))), (((-162 + 43) + (94 + 5)) + ((52 + -2) + (-29 + 0))))
    return Promise(x8Ynq53_.first, IU4__)

def X_54PnSx3(x8Ynq53_, IU4__):
    'g301503525q_yw1dL_6m637_saf'
    L_F75il2M(x8Ynq53_, ((0 + (-84 + 43)) + ((108 + -74) + (75 + -66))), (((-28 + -43) + (63 + -34)) + ((162 + -87) + (-99 + 68))))
    return Pair(o_Mv_g08D(x8Ynq53_.first, IU4__), P_s_o(x8Ynq53_.second, IU4__))
a2_08p0_0[(chr(99) + (str() + ('ons-strea' + 'm')))] = X_54PnSx3
a2_08p0_0[('' + (('' + 'de') + ('la' + 'y')))] = P_s_o

class c_139x5q(object):
    'B_QyQ72X_J_657AsR_7_'

    def __init__(OnB2B__, D8Ec4_01, IU4__):
        OnB2B__.D8Ec4_01 = D8Ec4_01
        OnB2B__.IU4__ = IU4__

def E6J4R_(V_J931iS, xP7_9BaX, IU4__):
    'V_87ahEo57_5u2na0Sa6tw91g'
    to7m1Mu_W = RCRH9I__(V_J931iS, xP7_9BaX, IU4__)
    if isinstance(to7m1Mu_W, c_139x5q):
        return o_Mv_g08D(to7m1Mu_W.D8Ec4_01, to7m1Mu_W.IU4__)
    else:
        return to7m1Mu_W

def x_uF15(oo_qM0YL7):
    'Ou71844u83rWiG4T_R1242zq'

    def h0_0U349C(D8Ec4_01, IU4__, Ha9x_nVD=False):
        'j90Z2_YWfzO4_Jto_1Xou1_o'
        if (Ha9x_nVD and (not L__2d69(D8Ec4_01)) and (not mow4478_9(D8Ec4_01))):
            return c_139x5q(D8Ec4_01, IU4__)
        q1Gj04i = c_139x5q(D8Ec4_01, IU4__)
        while isinstance(q1Gj04i, c_139x5q):
            (D8Ec4_01, IU4__) = (q1Gj04i.D8Ec4_01, q1Gj04i.IU4__)
            q1Gj04i = oo_qM0YL7(D8Ec4_01, IU4__)
        return q1Gj04i
    return h0_0U349C
o_Mv_g08D = x_uF15(o_Mv_g08D)

def A48Shd(Y__t, mt_q_, IU4__):
    mA79m(Y__t, tjf7_65Al, int((((0.0504173875466154 + 0.19386408373089625) + (-0.3818632631259452 + 0.8867943750975326)) * int((0.9020768967643847 * 0)))), (chr((127 + -18)) + ('' + ('' + 'ap'))))
    mA79m(mt_q_, SjS5gc8, (((-192 + 91) + (-29 + 46)) + ((202 + -74) + (45 + -88))), ((chr(109) + chr(97)) + 'p'))
    return mt_q_.map((lambda O1J7eT202: E6J4R_(Y__t, Pair(O1J7eT202, nil), IU4__)))

def G1r_(Y__t, mt_q_, IU4__):
    mA79m(Y__t, tjf7_65Al, 0, ('f' + (chr(105) + ('l' + 'ter'))))
    mA79m(mt_q_, SjS5gc8, (((-50 + 56) + (-130 + 69)) + ((6 + 99) + (-86 + 37))), ((('' + 'fil') + chr(116)) + ('' + ('' + 'er'))))
    (z_922f, current) = (nil, nil)
    while (mt_q_ is not nil):
        (el1x0491, mt_q_) = (mt_q_.first, mt_q_.second)
        if E6J4R_(Y__t, Pair(el1x0491, nil), IU4__):
            if (z_922f is nil):
                z_922f = Pair(el1x0491, nil)
                current = z_922f
            else:
                current.second = Pair(el1x0491, nil)
                current = current.second
    return z_922f

def AD_Knh(Y__t, mt_q_, IU4__):
    mA79m(Y__t, tjf7_65Al, int(((0.26341887348541604 + 0.27419869678438524) * 0)), (('' + ('' + 'red')) + ('' + ('u' + 'ce'))))
    mA79m(mt_q_, (lambda O1J7eT202: (O1J7eT202 is not nil)), (((-40 + 39) + (-99 + 22)) + ((-49 + 68) + (110 + -50))), (('r' + chr(101)) + (chr(100) + ('u' + 'ce'))))
    mA79m(mt_q_, SjS5gc8, (((92 + 23) + (-43 + -11)) + ((-92 + -23) + (7 + 48))), (str() + (('r' + 'e') + ('du' + 'ce'))))
    (kZ9O91gZy, mt_q_) = (mt_q_.first, mt_q_.second)
    while (mt_q_ is not nil):
        kZ9O91gZy = E6J4R_(Y__t, f898u99T(kZ9O91gZy, mt_q_.first), IU4__)
        mt_q_ = mt_q_.second
    return kZ9O91gZy

def Tl106(IH_V, IU4__, V9_9_=False, y9a_4_v6r=False, J_25AtW39=False, LD_4iS=(), Q3L9__=False):
    'I_0sGu_70NQS7Sb8t_EAX_A'
    if J_25AtW39:
        try:
            s_MJ8R(((chr(115) + ('che' + 'm')) + ('' + ('' + 'e_lib'))), True, IU4__)
        except Y6__:
            pass
        for x3f_w in LD_4iS:
            s_MJ8R(x3f_w, True, IU4__)
    while True:
        try:
            G3_91o4 = IH_V()
            while G3_91o4.F49_454J:
                qXk_8l_ = K5_e(G3_91o4)
                q1Gj04i = o_Mv_g08D(qXk_8l_, IU4__)
                if ((not y9a_4_v6r) and (q1Gj04i is not None)):
                    print(repl_str(q1Gj04i))
        except (Y6__, SyntaxError, ValueError, RuntimeError) as s_1_:
            if Q3L9__:
                if isinstance(s_1_, SyntaxError):
                    s_1_ = Y6__(s_1_)
                    raise s_1_
            b4l_3_gk(IU4__)
            if (isinstance(s_1_, RuntimeError) and (((('m' + 'a') + ('ximu' + 'm')) + ((' recursion' + ' de') + ('pth' + ' exceeded'))) not in getattr(s_1_, (chr((10 + 87)) + (chr(114) + ('' + 'gs'))))[int(((-0.25909479089566245 + 0.6534885334330011) * int((0.23844116631251422 * 0))))])):
                raise
            elif isinstance(s_1_, RuntimeError):
                print(((('Er' + 'ror: m') + ('aximum' + ' recursion d')) + (('' + 'ep') + ('th ex' + 'ceeded'))))
            else:
                print((str() + (('E' + 'rro') + ('r' + ':'))), s_1_)
        except KeyboardInterrupt:
            if (not J_25AtW39):
                raise
            IU4__.stack = []
            print()
            print(('' + (('Keyb' + 'oardInter') + ('r' + 'upt'))))
            if (not V9_9_):
                return
        except EOFError:
            print()
            return
Mcv9_3u = {
    ((str() + ('s' + 'e')) + chr((216 + -100))): ((('s' + 'e') + 't') + chr((120 + -87))),
}

def b4l_3_gk(IU4__):
    print(((('T' + 'raceback (most recent ') + ('ca' + 'll ')) + ('l' + ('ast)' + ':'))))
    for (U1_fu6q13, D8Ec4_01) in enumerate(IU4__.stack):
        print(((str() + (chr(32) + ' ')) + str(U1_fu6q13)), repl_str(D8Ec4_01), sep=chr(((-144 + 69) + (48 + 36))))
    IU4__.stack[:] = []

def s_MJ8R(*xP7_9BaX):
    'W_42__m5378p8y6kNF6__D86qH'
    if (not ((((-13 + -16) + (-29 + -24)) + ((19 + -32) + (112 + -15))) <= len(xP7_9BaX) <= (((67 + -50) + (2 + -35)) + ((-28 + 40) + (-36 + 43))))):
        x8Ynq53_ = xP7_9BaX[:(- (((274 + -83) + (-67 + -33)) + ((-126 + 28) + (17 + -9))))]
        raise Y6__(((('"' + 'lo') + ('ad" given ' + 'in')) + (('co' + 'rrect number of a') + ('rgu' + 'ments: {0}'))).format(len(x8Ynq53_)))
    YY__LMP_ = xP7_9BaX[int(((-0.6403757633425798 + 0.7138353168192049) * int((0.7199120130453319 * 0))))]
    y9a_4_v6r = (xP7_9BaX[(((224 + -98) + (-24 + -3)) + ((-4 + 5) + (-14 + -85)))] if (len(xP7_9BaX) > (((-83 + 44) + (-20 + 55)) + ((12 + 6) + (30 + -42)))) else True)
    IU4__ = xP7_9BaX[(- (((-145 + 94) + (1 + 48)) + ((-165 + 82) + (-13 + 99))))]
    if iv_aT(YY__LMP_):
        YY__LMP_ = eval(YY__LMP_)
    mA79m(YY__LMP_, L__2d69, int(((-0.17712012201917304 + 0.2741686036741572) * int((0.8596387974372722 * 0)))), ((chr(108) + ('' + 'oa')) + chr((109 + -9))))
    with Zy_Q3(YY__LMP_) as Bx_ERNR6:
        c9LiI29Z7 = Bx_ERNR6.readlines()
    xP7_9BaX = ((c9LiI29Z7, None) if y9a_4_v6r else (c9LiI29Z7,))

    def IH_V():
        return yo15431(*xP7_9BaX)
    e1_p_TAb = IU4__.stack[:]
    IU4__.stack[:] = []
    Tl106(IH_V, IU4__, y9a_4_v6r=y9a_4_v6r, Q3L9__=True)
    IU4__.stack[:] = e1_p_TAb

def Zy_Q3(x3f_w):
    'GCS7_3604eV91_4857Mg'
    try:
        return open(x3f_w)
    except IOError as j_84f34m:
        if x3f_w.endswith((('.' + 's') + ('' + ('' + 'cm')))):
            raise Y6__(str(j_84f34m))
    try:
        return open((x3f_w + (('.' + chr(115)) + (chr(99) + chr(109)))))
    except IOError as j_84f34m:
        raise Y6__(str(j_84f34m))

def Rpz5gz9d():
    'uf2T05D2Z4W24A13_d8_'
    IU4__ = c_XsKfu4u(None)
    IU4__.yJ3M06_((chr((2 + 99)) + ('' + ('va' + 'l'))), BuiltinProcedure(o_Mv_g08D, True, (chr((24 + 77)) + (('' + 'va') + 'l'))))
    IU4__.yJ3M06_((chr((181 + -84)) + ('' + ('ppl' + 'y'))), BuiltinProcedure(E6J4R_, True, (('' + ('a' + 'p')) + (('p' + 'l') + chr(121)))))
    IU4__.yJ3M06_((str() + (('' + 'loa') + chr(100))), BuiltinProcedure(s_MJ8R, True, (('l' + chr(111)) + (str() + ('' + 'ad')))))
    IU4__.yJ3M06_((str() + (('pro' + 'cedure') + '?')), BuiltinProcedure(tjf7_65Al, False, ((('' + 'proc') + ('' + 'ed')) + (chr(117) + ('r' + 'e?')))))
    IU4__.yJ3M06_(('' + (str() + ('' + 'map'))), BuiltinProcedure(A48Shd, True, (str() + (str() + ('m' + 'ap')))))
    IU4__.yJ3M06_(((('f' + 'il') + chr(116)) + ('' + ('' + 'er'))), BuiltinProcedure(G1r_, True, ((str() + ('f' + 'ilt')) + (chr(101) + chr(114)))))
    IU4__.yJ3M06_((chr((64 + 50)) + (('e' + 'du') + ('' + 'ce'))), BuiltinProcedure(AD_Knh, True, ((('' + 'red') + ('' + 'uc')) + chr(101))))
    IU4__.yJ3M06_(((str() + ('un' + 'def')) + (('i' + 'ne') + 'd')), None)
    IU4__.stack = []
    eN_46__2(IU4__, Ky5Q00)
    return IU4__

def O_Yu(*argv):
    import argparse
    f_XTp = argparse.ArgumentParser(description=(('C' + ('S 61A Scheme ' + 'Interpret')) + ('' + ('' + 'er'))))
    import __main__
    if ((('' + ('lo' + 'gi')) + 'c') in __main__.__file__):
        aYr__1Fo2 = (('L' + chr(111)) + ('g' + ('i' + 'c')))
    else:
        aYr__1Fo2 = ((('Sc' + 'h') + 'e') + ('m' + 'e'))
    version = __main__.__version__
    f_XTp.add_argument(('' + (('' + '--ver') + ('' + 'sion'))), action=((('v' + 'er') + ('s' + 'io')) + chr((158 + -48))), version=(chr(123) + '}').format(version))
    f_XTp.add_argument((('-' + ('' + '-dots-are-')) + (chr(99) + ('' + 'ons'))), action=((('s' + 't') + ('or' + 'e_')) + ('t' + ('ru' + 'e'))), help=((('run with pre-sp19 d' + 'o') + ('tt' + 'ed ')) + (('li' + 'st') + ('s behavior where dot' + 's are cons'))))
    f_XTp.add_argument((('' + ('-d' + 'eb')) + ('u' + chr(103))), (chr((-5 + 50)) + chr((41 + 59))), action=((('st' + 'ore_') + ('tr' + 'u')) + chr((100 + 1))), help=((('' + 'ex') + ('plo' + 're internal be')) + (('h' + 'a') + ('vior of the interpre' + 'ter'))))
    f_XTp.add_argument((str() + (str() + ('-l' + 'oad'))), (chr((-12 + 57)) + chr((63 + 42))), action=(('s' + ('t' + 'or')) + (str() + ('e_tr' + 'ue'))), help=((('r' + 'u') + ('n file ' + 'int')) + (('er' + 'a') + ('c' + 'tively'))))
    f_XTp.add_argument(((('' + 'fi') + chr(108)) + chr(101)), nargs=chr(63), type=argparse.FileType(chr(((129 + 56) + (-34 + -37)))), default=None, help=((('Scheme f' + 'i') + chr(108)) + ('' + ('e' + ' to run'))))
    xP7_9BaX = f_XTp.parse_args()
    import scheme
    scheme.DOTS_ARE_CONS = xP7_9BaX.dots_are_cons
    if (((('D' + ('ebug' + 'gin')) + (chr(103) + ('R' + 'un'))) not in globals()) and xP7_9BaX.debug):
        import scheme_debug
        scheme_debug.debug_run()
        return
    IH_V = iH5vN2j02
    V9_9_ = True
    LD_4iS = []
    if (xP7_9BaX.file is not None):
        if xP7_9BaX.load:
            LD_4iS.append(getattr(xP7_9BaX.file, (('n' + 'a') + ('' + ('m' + 'e')))))
        else:
            c9LiI29Z7 = xP7_9BaX.file.readlines()

            def IH_V():
                return yo15431(c9LiI29Z7)
            V9_9_ = False
    print(((('Welcome t' + 'o the CS 61A {}') + (' Interpreter (v' + 'ersion')) + ((' ' + '{}') + ')')).format(aYr__1Fo2, version))
    Tl106(IH_V, Rpz5gz9d(), J_25AtW39=True, V9_9_=V9_9_, LD_4iS=LD_4iS)
    O_8183()

