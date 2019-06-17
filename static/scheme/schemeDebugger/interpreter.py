
import code
import functools
import inspect
import re
import signal
import sys
import math
import math
import operator
import sys
import itertools
import string
import sys
import tokenize

# will be injected in debugging mode
'k61W3UfDcd_7__8Z4Rsy0_C2O86J3'

def w_1Fh30(LMft4_):
    'RDT7l35BMRI0_aKEHNFdF69J'
    if (inspect.stack()[(((-110 + 94) + (7 + 91)) + ((-61 + -29) + (75 + -66)))][int((((-0.5701448999050998 + 0.6910156158580445) + (0.6019681818371055 + 0.03296088431222377)) * 0))].f_locals[((str() + ('__na' + 'm')) + ('' + ('e_' + '_')))] == ((('' + '__m') + chr(97)) + (chr(105) + ('n' + '__')))):
        W1396B3xw = sys.argv[(((-161 + 19) + (127 + -51)) + ((117 + -2) + (-148 + 100))):]
        LMft4_(*W1396B3xw)
    return LMft4_
V2F7 = str()

def W3o6(LMft4_):
    'gPd621_25li4j1d_AnY7or19gY81'

    @functools.wraps(LMft4_)
    def c3WB850_(*W1396B3xw, **X9Vq2):
        global V2F7
        ZZht_18__ = [repr(S8wp3o) for S8wp3o in W1396B3xw]
        ZZht_18__ += [((repr(Ge_8m8) + chr(((-57 + 75) + (36 + 7)))) + repr(EMy9T_pc)) for (Ge_8m8, EMy9T_pc) in X9Vq2.items()]
        A4Y7((((('' + '{0}(') + chr(123)) + (str() + ('1' + '})'))).format(LMft4_.__name__, ('' + (chr(44) + chr(32))).join(ZZht_18__)) + chr(((171 + -55) + (-87 + 29)))))
        V2F7 += ((chr(32) + ' ') + (' ' + ' '))
        try:
            PR61 = LMft4_(*W1396B3xw, **X9Vq2)
            V2F7 = V2F7[:(- (((-133 + 81) + (2 + 95)) + ((89 + -88) + (-92 + 50))))]
        except Exception as S8wp3o:
            A4Y7((LMft4_.__name__ + ((' ' + ('exi' + 't')) + (('ed' + ' ') + ('via excep' + 'tion')))))
            V2F7 = V2F7[:(- (((48 + 69) + (-162 + 79)) + ((94 + -44) + (-122 + 42))))]
            raise
        A4Y7((str() + (('{' + '0}({1}) ->') + (' {' + '2}'))).format(LMft4_.__name__, (',' + chr((-18 + 50))).join(ZZht_18__), PR61))
        return PR61
    return c3WB850_

def A4Y7(Ie59t6):
    'XDLI_51_jZ1__5_9_68020l40a3'
    print((V2F7 + re.sub(chr((-43 + 53)), (chr(((31 + 17) + (5 + -43))) + V2F7), str(Ie59t6))))

def rt3__9():
    's_upj29zpZ7TLZ27a7_8d'
    s3Y9aI_w_ = inspect.stack()[(((32 + -59) + 0) + ((130 + -43) + (-75 + 16)))]
    A4Y7(((('Current' + ' line: File "') + '{') + (('f[1]}", line {f[' + '2]}, in') + (' {f[3' + ']}'))).format(f=s3Y9aI_w_))

def r0_1Ez_70(E5OO0GPSw=None):
    'v55CXJ__5Het641050jX_0'
    s3Y9aI_w_ = inspect.currentframe().f_back
    G9_9 = s3Y9aI_w_.f_globals.copy()
    G9_9.update(s3Y9aI_w_.f_locals)

    def h6MYP51Z_(signum, s3Y9aI_w_):
        print()
        exit(int((((-0.7024477690315966 + 0.47042359972933734) + (0.32861201846688914 + 0.493505223569529)) * int(((0.6053781222053992 + 0.31244568198202094) * int((0.6249146253653128 * 0)))))))
    signal.signal(signal.SIGINT, h6MYP51Z_)
    if (not E5OO0GPSw):
        (Tix5jx2, Y410yY, u_63615y, Tix5jx2, Tix5jx2, Tix5jx2) = inspect.stack()[(((117 + -29) + (-19 + 11)) + ((-67 + 48) + (-71 + 11)))]
        E5OO0GPSw = ((str() + ('In' + 'tera')) + (('cting at Fil' + 'e "{0}') + ('", line {1}' + ' \n'))).format(Y410yY, u_63615y)
        E5OO0GPSw += ((('  ' + '  Uni') + ('x:    <Cont' + 'rol>-D continues the pro')) + ('' + ('gram' + '; \n')))
        E5OO0GPSw += ((('    Windows: <Control' + '>-Z <Enter> continu') + ('es the progr' + 'am; ')) + chr(10))
        E5OO0GPSw += ((('    e' + 'xi') + ('t() or ' + '<Control>-C ex')) + (('its the pro' + 'gr') + ('' + 'am')))
    code.interact(E5OO0GPSw, None, G9_9)
'e1B0lUC16___NTzm5d79v'

class v_B2_G():
    'Zn3FFBuPX13_2i6A__hE11AI_25jZ'

    def __init__(Yipzrwt_o, E_KZ):
        Yipzrwt_o.index = int((0.3067631941113609 * 0))
        Yipzrwt_o.xi2_097 = []
        Yipzrwt_o.E_KZ = E_KZ
        Yipzrwt_o.current_line = ()
        Yipzrwt_o.current()

    def Xch2(Yipzrwt_o):
        'Evz5Gsdk3wA72o1QM9D_w'
        current = Yipzrwt_o.current()
        Yipzrwt_o.index += (((-49 + 60) + (106 + -100)) + ((105 + -23) + (-45 + -53)))
        return current

    def current(Yipzrwt_o):
        'R575S6_9m_DO9e338_01G'
        while (not Yipzrwt_o.OQFm):
            Yipzrwt_o.index = 0
            try:
                Yipzrwt_o.current_line = next(Yipzrwt_o.E_KZ)
                Yipzrwt_o.xi2_097.append(Yipzrwt_o.current_line)
            except StopIteration:
                Yipzrwt_o.current_line = ()
                return None
        return Yipzrwt_o.current_line[Yipzrwt_o.index]

    @property
    def OQFm(Yipzrwt_o):
        return (Yipzrwt_o.index < len(Yipzrwt_o.current_line))

    def __str__(Yipzrwt_o):
        'Et9b8_579__tTz9b8C_7_9h_8'
        P__O = len(Yipzrwt_o.xi2_097)
        E5OO0GPSw = (((str() + (('{' + '0:') + chr(62))) + str((math.floor(math.log10(P__O)) + (((148 + -60) + (-48 + 45)) + ((2 + -14) + (-51 + -21)))))) + ((chr(125) + ':') + chr((-29 + 61))))
        d988 = str()
        for v659 in range(max(int((((-0.7914108907184668 + 0.5739983621806867) + (-0.12279424508585246 + 0.4237943184072379)) * int(((-0.26887585653536916 + 0.453244817917538) * 0)))), (P__O - (((-5 + -6) + (-39 + 56)) + ((-132 + 50) + (40 + 40))))), (P__O - (((-156 + 96) + (-2 + -19)) + ((234 + -65) + (-183 + 96))))):
            d988 += ((E5OO0GPSw.format((v659 + (((80 + 3) + (10 + -40)) + ((-43 + 80) + (-173 + 84))))) + chr(32).join(map(str, Yipzrwt_o.xi2_097[v659]))) + '\n')
        d988 += E5OO0GPSw.format(P__O)
        d988 += chr(((180 + -54) + (-113 + 19))).join(map(str, Yipzrwt_o.current_line[:Yipzrwt_o.index]))
        d988 += (' ' + ('>' + ('>' + ' ')))
        d988 += chr((-28 + 60)).join(map(str, Yipzrwt_o.current_line[Yipzrwt_o.index:]))
        return d988.strip()
try:
    import readline
except:
    pass

class v8_59():
    'h5255_FLBR_84_3Iwi9k'

    def __init__(Yipzrwt_o, C6y0Pzs1G):
        Yipzrwt_o.C6y0Pzs1G = C6y0Pzs1G

    def __iter__(Yipzrwt_o):
        while True:
            (yield input(Yipzrwt_o.C6y0Pzs1G))
            Yipzrwt_o.C6y0Pzs1G = (chr((61 + -29)) * len(Yipzrwt_o.C6y0Pzs1G))

class ZBn5_k8():
    'f_4w_t0rt3UyJ22856_o9I0Ie8I'

    def __init__(Yipzrwt_o, xi2_097, C6y0Pzs1G, J_Q_co3=';'):
        Yipzrwt_o.xi2_097 = xi2_097
        Yipzrwt_o.C6y0Pzs1G = C6y0Pzs1G
        Yipzrwt_o.J_Q_co3 = J_Q_co3

    def __iter__(Yipzrwt_o):
        while Yipzrwt_o.xi2_097:
            u_63615y = Yipzrwt_o.xi2_097.pop(0).strip('\n')
            if ((Yipzrwt_o.C6y0Pzs1G is not None) and (u_63615y != str()) and (not u_63615y.lstrip().startswith(Yipzrwt_o.J_Q_co3))):
                print((Yipzrwt_o.C6y0Pzs1G + u_63615y))
                Yipzrwt_o.C6y0Pzs1G = (chr((-34 + 66)) * len(Yipzrwt_o.C6y0Pzs1G))
            (yield u_63615y)
        raise EOFError
'E1_5_w6BYpV7_H_15L6y949FuK'

class Pair():
    'mUK_k59_4B55_NV_0_AbmM3pV_seF'

    def __init__(Yipzrwt_o, p94cc908, U__BH):
        Yipzrwt_o.p94cc908 = p94cc908
        Yipzrwt_o.U__BH = U__BH

    def __repr__(Yipzrwt_o):
        return ((('Pair(' + '{') + ('' + '0}, ')) + (str() + ('' + '{1})'))).format(repr(Yipzrwt_o.p94cc908), repr(Yipzrwt_o.U__BH))

    def __str__(Yipzrwt_o):
        d988 = (chr((5 + 35)) + repl_str(Yipzrwt_o.p94cc908))
        U__BH = Yipzrwt_o.U__BH
        while isinstance(U__BH, Pair):
            d988 += (chr(((-130 + 76) + (95 + -9))) + repl_str(U__BH.p94cc908))
            U__BH = U__BH.U__BH
        if (U__BH is not nil):
            d988 += ((str() + (str() + (' .' + ' '))) + repl_str(U__BH))
        return (d988 + chr(((25 + 31) + (81 + -96))))

    def __len__(Yipzrwt_o):
        (P__O, U__BH) = ((((45 + -3) + (-138 + 74)) + ((121 + -62) + (-9 + -27))), Yipzrwt_o.U__BH)
        while isinstance(U__BH, Pair):
            P__O += (((-212 + 77) + (191 + -96)) + ((154 + -42) + (-80 + 9)))
            U__BH = U__BH.U__BH
        if (U__BH is not nil):
            raise TypeError(((('lengt' + 'h attempt') + ('ed on' + ' improper ')) + (('l' + 'is') + 't')))
        return P__O

    def __eq__(Yipzrwt_o, n_D3_):
        if (not isinstance(n_D3_, Pair)):
            return False
        return ((Yipzrwt_o.p94cc908 == n_D3_.p94cc908) and (Yipzrwt_o.U__BH == n_D3_.U__BH))

    def map(Yipzrwt_o, LMft4_):
        'jg13q2prL7_Q_T6jo_Q1'
        m_K9 = LMft4_(Yipzrwt_o.p94cc908)
        if ((Yipzrwt_o.U__BH is nil) or isinstance(Yipzrwt_o.U__BH, Pair)):
            return Pair(m_K9, Yipzrwt_o.U__BH.map(LMft4_))
        else:
            raise TypeError((('' + ('ill-f' + 'o')) + (('rme' + 'd') + (' lis' + 't'))))

class nil():
    'gZ01y_a5Vq98521811nLXe_3_'

    def __repr__(Yipzrwt_o):
        return ('n' + (str() + ('' + 'il')))

    def __str__(Yipzrwt_o):
        return (chr(40) + chr((139 + -98)))

    def __len__(Yipzrwt_o):
        return int((((-0.3637343036462479 + 0.4699668927381422) + (-0.3104913003848011 + 0.5878502275972345)) * int((0.9585284658206653 * 0))))

    def map(Yipzrwt_o, LMft4_):
        return Yipzrwt_o
nil = nil()
yZ9l7435 = {chr(39): ((('' + 'qu') + ('' + 'ot')) + chr((76 + 25))), chr(((-42 + 89) + (0 + 49))): ((('q' + 'uas') + chr(105)) + (('' + 'quot') + chr(101))), chr((8 + 36)): (('u' + ('' + 'nqu')) + (('' + 'ot') + chr(101))), (str() + (',' + chr(64))): ((('' + 'unquot') + ('e-s' + 'pl')) + (('' + 'ici') + ('' + 'ng')))}

def H_5yXx_(u722nW_0):
    'JXl_7s853Z1_6Do9_3_jl16'
    if (u722nW_0.current() is None):
        raise EOFError
    t_p8_4c0 = u722nW_0.Xch2()
    if (t_p8_4c0 == ('n' + ('i' + chr(108)))):
        return nil
    elif (t_p8_4c0 == chr(((10 + -65) + (135 + -40)))):
        return N53St(u722nW_0)
    elif (t_p8_4c0 in yZ9l7435):
        return Pair(yZ9l7435[t_p8_4c0], Pair(H_5yXx_(u722nW_0), nil))
    elif (t_p8_4c0 not in cN_3_np):
        return t_p8_4c0
    else:
        raise SyntaxError(((('' + 'un') + ('e' + 'x')) + (('p' + 'ected tok') + ('en:' + ' {0}'))).format(t_p8_4c0))

def N53St(u722nW_0):
    'Y28a75_E91_y5_bm11_27vExcC9j1'
    try:
        if (u722nW_0.current() is None):
            raise SyntaxError(((chr(117) + 'n') + (('expec' + 'ted end') + (' ' + 'of file'))))
        elif (u722nW_0.current() == ')'):
            u722nW_0.Xch2()
            return nil
        elif (u722nW_0.current() == '.'):
            u722nW_0.Xch2()
            By3f_ = H_5yXx_(u722nW_0)
            if (u722nW_0.current() is None):
                raise SyntaxError(((str() + ('un' + 'expe')) + (('cted end of ' + 'f') + ('i' + 'le'))))
            if (u722nW_0.Xch2() != chr(((-31 + 27) + (37 + 8)))):
                raise SyntaxError((('' + ('e' + 'x')) + (('pe' + 'cted one e') + ('leme' + 'nt after .'))))
            return By3f_
        else:
            p94cc908 = H_5yXx_(u722nW_0)
            R0_0o = N53St(u722nW_0)
            return Pair(p94cc908, R0_0o)
    except EOFError:
        raise SyntaxError(((('unexpe' + 'c') + 't') + (('e' + 'd') + (' end of' + ' file'))))

def S0G98Hy(C6y0Pzs1G='scm> '):
    'v_gNlqDB3D28rG9z_BFGJL0krG_'
    return v_B2_G(E93_r3A_N(v8_59(C6y0Pzs1G)))

def Zy_Q3(xi2_097, C6y0Pzs1G='scm> ', Qr_2=False):
    's___6G29oe7x__Tu48861706_'
    if Qr_2:
        hrx_gaO0 = xi2_097
    else:
        hrx_gaO0 = ZBn5_k8(xi2_097, C6y0Pzs1G)
    return v_B2_G(E93_r3A_N(hrx_gaO0))

def z__f34(u_63615y):
    'xi73It45J846_er2f1_2'
    return H_5yXx_(v_B2_G(E93_r3A_N([u_63615y])))

def repl_str(t_p8_4c0):
    'RP_p_36_v85940e_7D3h6uzge9'
    if (t_p8_4c0 is True):
        return (str() + (str() + ('#' + 't')))
    if (t_p8_4c0 is False):
        return (str() + (chr(35) + chr(102)))
    if (t_p8_4c0 is None):
        return (('u' + chr(110)) + ('' + ('d' + 'efined')))
    return str(t_p8_4c0)

def oU2O_2897():
    'c1_009G7i4919aAEn_Um0'
    while True:
        try:
            u722nW_0 = S0G98Hy(((chr(114) + ('e' + 'a')) + ('d' + ('' + '> '))))
            while u722nW_0.OQFm:
                el1x0491 = H_5yXx_(u722nW_0)
                print((chr(115) + (('' + 'tr') + ('' + ' :'))), el1x0491)
                print(((chr(114) + 'e') + (str() + ('pr' + ':'))), repr(el1x0491))
        except (SyntaxError, ValueError) as SjS5gc8:
            print((type(SjS5gc8).__name__ + chr(((231 + -84) + (-28 + -61)))), SjS5gc8)
        except (KeyboardInterrupt, EOFError):
            print()
            return
'p15_E022__830_b70CT7_5'
try:
    import turtle
    import tkinter
except:
    print(((('warn' + 'ing: ') + ('could' + ' not')) + ('' + (' import the turt' + 'le module.'))), file=sys.stderr)

class tHw1_52C4(Exception):
    'lfq1WL7F44n9_270b6489QD56_2_n'
L__2d69 = []

def j6Kg2(*YglxiK8HA):
    'yO153I_PnR7I19Z6l_UF69'

    def add(LMft4_):
        for K60___u0 in YglxiK8HA:
            L__2d69.append((K60___u0, LMft4_, YglxiK8HA[int(((0.46470718736779826 + 0.12891305180284396) * 0))]))
        return LMft4_
    return add

def cBQ_4(t_p8_4c0, qS4Sz_n, Ge_8m8, K60___u0):
    'tf9485J35A198qA6ioY7__1'
    if (not qS4Sz_n(t_p8_4c0)):
        E5OO0GPSw = ((('arg' + 'um') + ('ent {0}' + ' ')) + (('of {1} has wrong type' + ' ') + ('({2}' + ')')))
        raise tHw1_52C4(E5OO0GPSw.format(Ge_8m8, K60___u0, type(t_p8_4c0).__name__))
    return t_p8_4c0

@j6Kg2((('b' + ('o' + 'o')) + (('l' + 'e') + ('an' + '?'))))
def n71Ld_(h0_0U349C):
    return ((h0_0U349C is True) or (h0_0U349C is False))

def b7WA00(t_p8_4c0):
    'T1_2c15KHFraGZ411GK6BmSQu'
    return (t_p8_4c0 is not False)

def i_Bv_r0_5(t_p8_4c0):
    'o9_K6Nq111s41JJ7_1a5_f83SEkB_'
    return (t_p8_4c0 is False)

@j6Kg2(('n' + (str() + ('' + 'ot'))))
def T9x_G4699(h0_0U349C):
    return (not b7WA00(h0_0U349C))

@j6Kg2(((('eq' + 'u') + chr(97)) + (str() + ('' + 'l?'))))
def J_48(h0_0U349C, UWL2oUi_t):
    if (H3pGJGl(h0_0U349C) and H3pGJGl(UWL2oUi_t)):
        return (J_48(h0_0U349C.p94cc908, UWL2oUi_t.p94cc908) and J_48(h0_0U349C.U__BH, UWL2oUi_t.U__BH))
    elif (fkS4(h0_0U349C) and fkS4(UWL2oUi_t)):
        return (h0_0U349C == UWL2oUi_t)
    else:
        return ((type(h0_0U349C) == type(UWL2oUi_t)) and (h0_0U349C == UWL2oUi_t))

@j6Kg2((('e' + chr(113)) + chr((109 + -46))))
def EQ002sM(h0_0U349C, UWL2oUi_t):
    if (fkS4(h0_0U349C) and fkS4(UWL2oUi_t)):
        return (h0_0U349C == UWL2oUi_t)
    elif (G3_91o4(h0_0U349C) and G3_91o4(UWL2oUi_t)):
        return (h0_0U349C == UWL2oUi_t)
    else:
        return (h0_0U349C is UWL2oUi_t)

@j6Kg2((('p' + 'a') + ('i' + ('' + 'r?'))))
def H3pGJGl(h0_0U349C):
    return isinstance(h0_0U349C, Pair)

@j6Kg2(((chr(112) + 'r') + (('' + 'om') + ('' + 'ise?'))))
def l7g30_(h0_0U349C):
    return (type(h0_0U349C).__name__ == ((chr(80) + 'r') + (('o' + 'm') + ('i' + 'se'))))

@j6Kg2((('f' + ('o' + 'r')) + (str() + ('' + 'ce'))))
def x_3_(h0_0U349C):
    cBQ_4(h0_0U349C, l7g30_, int(((-0.6788405790601449 + 0.9113543365562695) * int((0.8702427378100142 * 0)))), ('p' + (('' + 'romis') + 'e')))
    return h0_0U349C.M_0R0_()

@j6Kg2((('c' + ('dr' + '-')) + (str() + ('stre' + 'am'))))
def JA249(h0_0U349C):
    cBQ_4(h0_0U349C, (lambda h0_0U349C: (H3pGJGl(h0_0U349C) and l7g30_(h0_0U349C.U__BH))), int((((-1.2852102920175235 + 0.9638638278004978) + (0.1315641047558228 + 0.193681640746739)) * int(((-0.12997322462790162 + 0.186801185026374) * int((0.8042069950743564 * 0)))))), ((('' + 'cdr') + ('-' + 's')) + (('t' + 're') + ('a' + 'm'))))
    return x_3_(h0_0U349C.U__BH)

@j6Kg2(('n' + (chr(117) + ('' + 'll?'))))
def S82T(h0_0U349C):
    return (h0_0U349C is nil)

@j6Kg2(((('' + 'lis') + chr(116)) + '?'))
def nFZ5(h0_0U349C):
    'nW_5Dx_g__e_p80VBpqbC48089DC'
    while (h0_0U349C is not nil):
        if (not isinstance(h0_0U349C, Pair)):
            return False
        h0_0U349C = h0_0U349C.U__BH
    return True

@j6Kg2(('l' + ('' + ('en' + 'gth'))))
def jLh9d_O(h0_0U349C):
    cBQ_4(h0_0U349C, nFZ5, 0, ((('' + 'len') + chr(103)) + ('' + ('' + 'th'))))
    if (h0_0U349C is nil):
        return int((((-0.844492100384147 + 0.5244822392369944) + (-0.20900029074493887 + 0.7710241102518038)) * int((0.6573257921664376 * 0))))
    return len(h0_0U349C)

@j6Kg2((('' + ('' + 'con')) + chr((153 + -38))))
def O1_nj(h0_0U349C, UWL2oUi_t):
    return Pair(h0_0U349C, UWL2oUi_t)

@j6Kg2((str() + (chr(99) + ('' + 'ar'))))
def eoy_(h0_0U349C):
    cBQ_4(h0_0U349C, H3pGJGl, int((((0.052456621431704376 + 0.531736841358057) + (-0.203178122300957 + 0.38226392992828007)) * int((0.08718122269217587 * 0)))), (str() + (('' + 'ca') + 'r')))
    return h0_0U349C.p94cc908

@j6Kg2((chr(99) + (str() + ('d' + 'r'))))
def F27Z_(h0_0U349C):
    cBQ_4(h0_0U349C, H3pGJGl, int(((0.4584907201214854 + 0.06667680965488221) * 0)), (chr(99) + (str() + ('d' + 'r'))))
    return h0_0U349C.U__BH

@j6Kg2(((('se' + 't') + ('-' + 'car')) + chr((121 + -88))))
def eoy_(h0_0U349C, UWL2oUi_t):
    cBQ_4(h0_0U349C, H3pGJGl, int((((0.5776742992728734 + 0.3328227430157742) + (-0.12568339265261264 + 0.1477789997485729)) * int(((0.8165409437503263 + 0.1819838933543776) * int((0.7258823987632143 * 0)))))), (('' + ('' + 'se')) + (('t-c' + 'a') + ('r' + '!'))))
    h0_0U349C.p94cc908 = UWL2oUi_t

@j6Kg2(((('set-' + 'c') + chr(100)) + (chr(114) + chr(33))))
def F27Z_(h0_0U349C, UWL2oUi_t):
    cBQ_4(h0_0U349C, H3pGJGl, int((((-0.5080396984044535 + 0.5394355188795696) + (-0.3638656472655091 + 0.39851416394127004)) * int(((-0.5882583088269816 + 0.7835870068487014) * 0)))), (str() + (('se' + 't-cd') + ('' + 'r!'))))
    h0_0U349C.U__BH = UWL2oUi_t

@j6Kg2((str() + ('l' + ('i' + 'st'))))
def wq8_(*rj_L_8):
    PR61 = nil
    for S8wp3o in reversed(rj_L_8):
        PR61 = Pair(S8wp3o, PR61)
    return PR61

@j6Kg2((('a' + 'p') + (('p' + 'e') + ('' + 'nd'))))
def izgR11K_n(*rj_L_8):
    if (len(rj_L_8) == int(((-0.21305475683412034 + 0.2758126932141265) * 0))):
        return nil
    PR61 = rj_L_8[(- (((140 + -61) + (1 + -7)) + ((-151 + 84) + (-15 + 10))))]
    for v659 in range((len(rj_L_8) - (((-22 + -53) + (-47 + 55)) + ((97 + 21) + (7 + -56)))), (- (((-122 + 97) + (68 + 18)) + ((4 + -99) + (49 + -14)))), (- (((31 + -29) + (146 + -78)) + ((-27 + 54) + (-22 + -74))))):
        EMy9T_pc = rj_L_8[v659]
        if (EMy9T_pc is not nil):
            cBQ_4(EMy9T_pc, H3pGJGl, v659, ((('a' + 'p') + chr(112)) + (('' + 'en') + chr(100))))
            xUX_c_ = n_D3_ = Pair(EMy9T_pc.p94cc908, PR61)
            EMy9T_pc = EMy9T_pc.U__BH
            while H3pGJGl(EMy9T_pc):
                n_D3_.U__BH = Pair(EMy9T_pc.p94cc908, PR61)
                n_D3_ = n_D3_.U__BH
                EMy9T_pc = EMy9T_pc.U__BH
            PR61 = xUX_c_
    return PR61

@j6Kg2(((str() + ('st' + 'r')) + ('' + ('i' + 'ng?'))))
def L5e__s8GH(h0_0U349C):
    return (isinstance(h0_0U349C, str) and h0_0U349C.startswith(chr(((-28 + 63) + (-18 + 17)))))

@j6Kg2((('' + ('' + 'symb')) + (('' + 'ol') + chr(63))))
def G3_91o4(h0_0U349C):
    return (isinstance(h0_0U349C, str) and (not L5e__s8GH(h0_0U349C)))

@j6Kg2((str() + (chr(110) + ('umb' + 'er?'))))
def fkS4(h0_0U349C):
    return (isinstance(h0_0U349C, (int, float)) and (not n71Ld_(h0_0U349C)))

@j6Kg2((chr((203 + -98)) + (('n' + 'teg') + ('' + 'er?'))))
def u_8__x54B(h0_0U349C):
    return (fkS4(h0_0U349C) and (isinstance(h0_0U349C, int) or (round(h0_0U349C) == h0_0U349C)))

def d__2_Lq42(*rj_L_8):
    'U_QI53VM2_B_8_dj0fi5__15'
    for (v659, EMy9T_pc) in enumerate(rj_L_8):
        if (not fkS4(EMy9T_pc)):
            E5OO0GPSw = ((('oper' + 'and {0') + ('} ' + '({1')) + (('' + '})') + (' is not a numbe' + 'r')))
            raise tHw1_52C4(E5OO0GPSw.format(v659, EMy9T_pc))

def m6it(LMft4_, L8g7D, rj_L_8):
    'B_3_46_s92P5E4674v2__'
    d__2_Lq42(*rj_L_8)
    d988 = L8g7D
    for t_p8_4c0 in rj_L_8:
        d988 = LMft4_(d988, t_p8_4c0)
    if (round(d988) == d988):
        d988 = round(d988)
    return d988

@j6Kg2(chr((36 + 7)))
def P587_52(*rj_L_8):
    return m6it(operator.add, int((((-0.01678433083247899 + 0.3060649552540319) + (0.1449254479727583 + 0.4984591315792676)) * int(((-0.5188128963184314 + 0.9381818384439552) * int((0.23114783293418983 * 0)))))), rj_L_8)

@j6Kg2(chr(((74 + -20) + (16 + -25))))
def X_m206(v0_s5__, *rj_L_8):
    d__2_Lq42(v0_s5__, *rj_L_8)
    if (len(rj_L_8) == int(((0.6166242142804385 + 0.3470232230519189) * int((0.09863833481635687 * 0))))):
        return (- v0_s5__)
    return m6it(operator.sub, v0_s5__, rj_L_8)

@j6Kg2(chr(42))
def Q3m6_1(*rj_L_8):
    return m6it(operator.mul, (((-85 + 79) + (-35 + 18)) + ((187 + -70) + (3 + -96))), rj_L_8)

@j6Kg2(chr(((43 + -86) + (17 + 73))))
def y_A__b(v0_s5__, *rj_L_8):
    d__2_Lq42(v0_s5__, *rj_L_8)
    try:
        if (len(rj_L_8) == int((((0.005316827814661029 + 0.24433971100248963) + (-0.24226284006346055 + 0.8801464772723284)) * int(((0.2601982218208706 + 0.06665067967521099) * int((0.11424298906467278 * 0))))))):
            return ((((-52 + 69) + (-112 + 20)) + ((-5 + 48) + (59 + -26))) / v0_s5__)
        return m6it(operator.truediv, v0_s5__, rj_L_8)
    except ZeroDivisionError as SjS5gc8:
        raise tHw1_52C4(SjS5gc8)

@j6Kg2(((str() + ('e' + 'x')) + ('p' + 't')))
def nY9HrRo23(v0_s5__, Y7k5_):
    d__2_Lq42(v0_s5__, Y7k5_)
    return pow(v0_s5__, Y7k5_)

@j6Kg2(('' + (('a' + 'b') + 's')))
def v9l51(v0_s5__):
    return abs(v0_s5__)

@j6Kg2(((str() + ('' + 'quotie')) + (chr(110) + 't')))
def yO9t3_(v0_s5__, Y7k5_):
    d__2_Lq42(v0_s5__, Y7k5_)
    try:
        return int((v0_s5__ / Y7k5_))
    except ZeroDivisionError as SjS5gc8:
        raise tHw1_52C4(SjS5gc8)

@j6Kg2(((('m' + 'od') + ('' + 'ul')) + chr((145 + -34))))
def j__Q0(v0_s5__, Y7k5_):
    d__2_Lq42(v0_s5__, Y7k5_)
    try:
        return (v0_s5__ % Y7k5_)
    except ZeroDivisionError as SjS5gc8:
        raise tHw1_52C4(SjS5gc8)

@j6Kg2(((str() + ('rem' + 'a')) + ('i' + ('n' + 'der'))))
def i5KKo4x(v0_s5__, Y7k5_):
    d__2_Lq42(v0_s5__, Y7k5_)
    try:
        PR61 = (v0_s5__ % Y7k5_)
    except ZeroDivisionError as SjS5gc8:
        raise tHw1_52C4(SjS5gc8)
    while (((PR61 < 0) and (v0_s5__ > int((((-0.47342452965931703 + 0.9621104975943422) + (0.18389494599750722 + 0.05612453440618037)) * 0)))) or ((PR61 > int((0.06553699593354778 * 0))) and (v0_s5__ < int((0.33894891049455844 * 0))))):
        PR61 -= Y7k5_
    return PR61

def v_7_7xG__(Qe63_, K60___u0):
    'e9rA__v__91_HI1_M_8_'
    mt5f8 = getattr(Qe63_, K60___u0)

    def Yi3Zt_(*rj_L_8):
        d__2_Lq42(*rj_L_8)
        return mt5f8(*rj_L_8)
    return Yi3Zt_
for DqU5 in [(str() + (('' + 'ac') + ('o' + 's'))), ((chr(97) + chr(99)) + (('o' + 's') + 'h')), (('' + ('a' + 's')) + ('i' + 'n')), (('a' + ('s' + 'in')) + chr((92 + 12))), ((str() + ('at' + 'a')) + 'n'), ((('' + 'at') + 'a') + ('n' + '2')), (chr((171 + -74)) + (('t' + 'a') + ('n' + 'h'))), (str() + (chr(99) + ('' + 'eil'))), ((chr(99) + ('' + 'opys')) + ('i' + ('' + 'gn'))), (chr(99) + ('' + ('' + 'os'))), (('c' + ('' + 'os')) + chr((115 + -11))), ((('d' + 'e') + chr(103)) + (('' + 're') + ('' + 'es'))), ((('' + 'fl') + chr(111)) + (str() + ('o' + 'r'))), ('' + (chr(108) + ('' + 'og'))), ((chr(108) + chr(111)) + ('g' + ('1' + '0'))), ((('' + 'log') + chr(49)) + chr((181 + -69))), (('' + ('' + 'lo')) + ('' + ('' + 'g2'))), (('' + ('' + 'ra')) + (('' + 'di') + ('' + 'ans'))), ('' + (chr(115) + ('i' + 'n'))), (str() + (('s' + 'in') + chr(104))), (('' + ('sq' + 'r')) + chr((123 + -7))), (str() + (('' + 'ta') + 'n')), (chr(116) + ('' + ('' + 'anh'))), (str() + (('t' + 'r') + ('' + 'unc')))]:
    j6Kg2(DqU5)(v_7_7xG__(math, DqU5))

def cpw3Gs(mM_0eCF8M, h0_0U349C, UWL2oUi_t):
    d__2_Lq42(h0_0U349C, UWL2oUi_t)
    return mM_0eCF8M(h0_0U349C, UWL2oUi_t)

@j6Kg2(chr(61))
def l_cRQ(h0_0U349C, UWL2oUi_t):
    return cpw3Gs(operator.eq, h0_0U349C, UWL2oUi_t)

@j6Kg2(chr((113 + -53)))
def q94Q4_2i(h0_0U349C, UWL2oUi_t):
    return cpw3Gs(operator.lt, h0_0U349C, UWL2oUi_t)

@j6Kg2(chr(62))
def J06F2(h0_0U349C, UWL2oUi_t):
    return cpw3Gs(operator.gt, h0_0U349C, UWL2oUi_t)

@j6Kg2((str() + (str() + ('' + '<='))))
def S8yIW(h0_0U349C, UWL2oUi_t):
    return cpw3Gs(operator.le, h0_0U349C, UWL2oUi_t)

@j6Kg2((chr((118 + -56)) + chr(61)))
def w9W2I(h0_0U349C, UWL2oUi_t):
    return cpw3Gs(operator.ge, h0_0U349C, UWL2oUi_t)

@j6Kg2(('e' + (('ve' + 'n') + '?')))
def aa7ayLM6(h0_0U349C):
    d__2_Lq42(h0_0U349C)
    return ((h0_0U349C % (((74 + -5) + (-24 + 39)) + ((-257 + 90) + (183 + -98)))) == 0)

@j6Kg2((str() + (('od' + 'd') + '?')))
def N0LY_(h0_0U349C):
    d__2_Lq42(h0_0U349C)
    return ((h0_0U349C % (((71 + 28) + (43 + -100)) + ((-56 + 93) + (-29 + -48)))) == (((47 + -95) + (-132 + 82)) + ((165 + -33) + (20 + -53))))

@j6Kg2(((('' + 'ze') + 'r') + ('' + ('o' + '?'))))
def W68a70(h0_0U349C):
    d__2_Lq42(h0_0U349C)
    return (h0_0U349C == int((((-0.33473135307364066 + 0.3995391992043804) + (0.059804400440434446 + 0.3392321202982853)) * int((0.31710353781118605 * 0)))))

@j6Kg2(((chr(97) + 't') + ('' + ('om' + '?'))))
def NvB_k7(h0_0U349C):
    return (n71Ld_(h0_0U349C) or fkS4(h0_0U349C) or G3_91o4(h0_0U349C) or S82T(h0_0U349C))

@j6Kg2((('' + ('di' + 'spl')) + (chr(97) + 'y')))
def bh2bO_UR(t_p8_4c0):
    if L5e__s8GH(t_p8_4c0):
        t_p8_4c0 = eval(t_p8_4c0)
    print(repl_str(t_p8_4c0), end='')

@j6Kg2(((('p' + 'r') + 'i') + ('n' + chr(116))))
def Q799wUe8(t_p8_4c0):
    print(repl_str(t_p8_4c0))

@j6Kg2(((chr(110) + ('ew' + 'l')) + ('' + ('i' + 'ne'))))
def x4U11_8fB():
    print()
    sys.stdout.flush()

@j6Kg2(((chr(101) + ('' + 'rr')) + (chr(111) + 'r')))
def J8446(E5OO0GPSw=None):
    E5OO0GPSw = (str() if (E5OO0GPSw is None) else repl_str(E5OO0GPSw))
    raise tHw1_52C4(E5OO0GPSw)

@j6Kg2(('' + ('e' + ('' + 'xit'))))
def S1eb():
    raise EOFError
d_725 = False
KqW_zd28 = True

def h8Q8q901():
    return d_725

def EcMV856():
    global d_725
    if (not d_725):
        d_725 = True
        turtle.title(((('Sc' + 'heme') + ('' + ' T')) + (('' + 'ur') + ('tle' + 's'))))
        turtle.mode((('l' + chr(111)) + (chr(103) + chr(111))))

@j6Kg2(((chr(102) + 'o') + (('' + 'rwa') + ('r' + 'd'))), (str() + ('' + ('f' + 'd'))))
def d6_034Y(P__O):
    'i__AIB_aO_7N7_9761aa_47oG'
    d__2_Lq42(P__O)
    EcMV856()
    turtle.forward(P__O)

@j6Kg2((chr(98) + (('' + 'ackwa') + ('' + 'rd'))), ((('' + 'ba') + 'c') + chr((55 + 52))), (chr((1 + 97)) + chr(107)))
def B3np70_Yq(P__O):
    'u0__54i5u71_b6___0E6'
    d__2_Lq42(P__O)
    EcMV856()
    turtle.backward(P__O)

@j6Kg2((chr((165 + -57)) + (str() + ('ef' + 't'))), ('' + ('' + ('' + 'lt'))))
def Y19ey90M1(P__O):
    'VzQ5t34kuBD6_9EFJ68e5'
    d__2_Lq42(P__O)
    EcMV856()
    turtle.left(P__O)

@j6Kg2(('r' + (('ig' + 'h') + chr(116))), (str() + (chr(114) + chr(116))))
def iV_5zB(P__O):
    'T8K7K2P6XM9_29jsH437d65'
    d__2_Lq42(P__O)
    EcMV856()
    turtle.right(P__O)

@j6Kg2((('c' + ('i' + 'r')) + (('' + 'cl') + chr(101))))
def K4VV7h__6(xUX_c_, S4fCN614_=None):
    'A3_8012U_7p_a04UJ8K5q5ux_e3fs'
    if (S4fCN614_ is None):
        d__2_Lq42(xUX_c_)
    else:
        d__2_Lq42(xUX_c_, S4fCN614_)
    EcMV856()
    turtle.circle(xUX_c_, (S4fCN614_ and S4fCN614_))

@j6Kg2(((str() + ('se' + 't')) + (('p' + 'ositi') + ('' + 'on'))), (('s' + ('' + 'et')) + (('p' + 'o') + 's')), ('' + (chr(103) + ('ot' + 'o'))))
def M_x_7(h0_0U349C, UWL2oUi_t):
    'bW5b_U42_MT_3_0_jPN0719983'
    d__2_Lq42(h0_0U349C, UWL2oUi_t)
    EcMV856()
    turtle.setposition(h0_0U349C, UWL2oUi_t)

@j6Kg2((('' + ('sethead' + 'in')) + chr(103)), (chr((208 + -93)) + (('e' + 't') + 'h')))
def t37kIEL(J8P_):
    'h4X99ZI77VGx5_0nc5_QjzL'
    d__2_Lq42(J8P_)
    EcMV856()
    turtle.setheading(J8P_)

@j6Kg2(((('' + 'pe') + chr(110)) + (str() + ('u' + 'p'))), (chr(112) + chr((142 + -25))))
def mm88vm1__():
    'b2494Y3_Z_AD76fG286w'
    EcMV856()
    turtle.penup()

@j6Kg2(((('p' + 'endo') + chr(119)) + chr((126 + -16))), (chr((137 + -25)) + chr(100)))
def E5dqdw():
    's_IC_DO_9Cz7665B3l0_0k7fS4oa'
    EcMV856()
    turtle.pendown()

@j6Kg2((('s' + ('how' + 't')) + (('' + 'urt') + ('' + 'le'))), (chr((120 + -5)) + chr((170 + -54))))
def E7MW_5E():
    'YA09Ns01aw7UYi_j2Vjj8d_q2262'
    EcMV856()
    turtle.showturtle()

@j6Kg2(('h' + (chr(105) + ('detu' + 'rtle'))), (str() + ('h' + chr(116))))
def b43Wly4n6():
    'a_0966l6W2jXo__8457s'
    EcMV856()
    turtle.hideturtle()

@j6Kg2(((('c' + 'l') + chr(101)) + ('' + ('' + 'ar'))))
def qO8_():
    'gEEs__ixz1Y_PD249_UM27I060L'
    EcMV856()
    turtle.clear()

@j6Kg2((str() + (('' + 'co') + ('' + 'lor'))))
def V57IH5(yc2mB10t):
    'u_JU_e1_9_8f8R2_7sDq52d0'
    EcMV856()
    cBQ_4(yc2mB10t, L5e__s8GH, int((0.7307342357845545 * 0)), (chr((156 + -57)) + (('' + 'olo') + chr(114))))
    turtle.color(eval(yc2mB10t))

@j6Kg2(('r' + (str() + ('g' + 'b'))))
def lRC_(HZ_M_03KO, t_521_V, GR_v1_23):
    'xk36Y51avnx_2_5B7_B32d4z_8_'
    oM291 = (HZ_M_03KO, t_521_V, GR_v1_23)
    for h0_0U349C in oM291:
        if ((h0_0U349C < int(((-0.43802835496921366 + 0.9445727138290241) * int((0.6481713320322876 * 0))))) or (h0_0U349C > (((56 + -58) + (152 + -66)) + ((-84 + 7) + (-38 + 32))))):
            raise tHw1_52C4((((('I' + 'lle') + ('gal' + ' c')) + (('olor intens' + 'ity ') + ('' + 'in '))) + repl_str(oM291)))
    ogpY9 = tuple((int((h0_0U349C * (((219 + 90) + (123 + -77)) + ((-100 + -87) + (177 + -90))))) for h0_0U349C in oM291))
    return (((('"#%02x%0' + '2x%') + ('0' + '2')) + (chr(120) + chr(34))) % ogpY9)

@j6Kg2(((str() + ('b' + 'e')) + (('' + 'gin') + ('_f' + 'ill'))))
def n36f():
    'u0451E_N82V3L9I76__F_8y0v6'
    EcMV856()
    turtle.begin_fill()

@j6Kg2((str() + ('e' + ('' + 'nd_fill'))))
def jtE9qdy():
    'C0ABGoCD3x_43y2__p8j8Ulj4bl8'
    EcMV856()
    turtle.end_fill()

@j6Kg2(((('b' + 'gc') + ('o' + 'l')) + (chr(111) + chr(114))))
def QF3i0(yc2mB10t):
    EcMV856()
    cBQ_4(yc2mB10t, L5e__s8GH, int((0.2318815123305733 * 0)), ((str() + ('' + 'bg')) + ('c' + ('olo' + 'r'))))
    turtle.bgcolor(eval(yc2mB10t))

@j6Kg2((str() + (str() + ('exiton' + 'click'))))
def U_3r30():
    'MV_6A02V0_4pw4w_C8_9__3Fj__1A'
    global d_725
    if (KqW_zd28 and d_725):
        print(((('Clos' + 'e or click on ') + ('turtle wind' + 'ow to comple')) + ('t' + ('e' + ' exit'))))
        turtle.exitonclick()
        d_725 = False

@j6Kg2(((str() + ('s' + 'pe')) + ('e' + 'd')))
def nq_suO69(d988):
    'vs5E23SB16VQQy_415181W8Q'
    cBQ_4(d988, u_8__x54B, 0, (('s' + chr(112)) + (('' + 'ee') + chr(100))))
    EcMV856()
    turtle.speed(d988)

@j6Kg2(((str() + ('' + 'pi')) + (str() + ('xe' + 'l'))))
def h02_D(h0_0U349C, UWL2oUi_t, yc2mB10t):
    'x099cN6Bp4UyxY_7qw47b___15'
    cBQ_4(yc2mB10t, L5e__s8GH, int((((-0.15382330615300766 + 0.383129587974784) + (-0.4683951797741821 + 0.57544954815758)) * int(((-0.6400289901221478 + 0.7603699786082394) * 0)))), (chr(112) + ('i' + ('' + 'xel'))))
    N_3_ = eval(yc2mB10t)
    p_4Mn_Q2 = turtle.getcanvas()
    (Q_8NGw3L, J8P_) = (p_4Mn_Q2.winfo_width(), p_4Mn_Q2.winfo_height())
    if (not hasattr(h02_D, (('' + ('' + 'ima')) + (chr(103) + 'e')))):
        EcMV856()
        h02_D.image = tkinter.PhotoImage(width=Q_8NGw3L, height=J8P_)
        p_4Mn_Q2.create_image((int((0.6638334285611124 * 0)), int((0.5325054511657719 * 0))), image=h02_D.image, state=((chr(110) + ('o' + 'r')) + ('' + ('m' + 'al'))))
    M288_O = h02_D.M288_O
    for I8r_c1T in range(M288_O):
        for M21m in range(M288_O):
            (Z_W557, wr8W0_) = (((h0_0U349C * M288_O) + I8r_c1T), (J8P_ - ((UWL2oUi_t * M288_O) + M21m)))
            if ((int((((0.4084788593156935 + 0.3349450921264917) + (0.17693574535719947 + 0.05764627924676313)) * int(((0.5512927629383556 + 0.08936501112594264) * int((0.3805125980358146 * 0)))))) < Z_W557 < Q_8NGw3L) and (0 < wr8W0_ < J8P_)):
                h02_D.image.put(N_3_, (Z_W557, wr8W0_))
h02_D.M288_O = (((68 + -93) + (99 + -45)) + ((131 + -85) + (-64 + -10)))

@j6Kg2((chr(112) + (('ixel' + 'si') + ('' + 'ze'))))
def Fb94__6t4(M288_O):
    'S79UM51ObXjM8v_w44F_gRN5N'
    d__2_Lq42(M288_O)
    if ((M288_O <= 0) or (not isinstance(M288_O, int))):
        raise tHw1_52C4((((('I' + 'nv') + ('alid pix' + 'el size:')) + ' ') + repl_str(M288_O)))
    h02_D.M288_O = M288_O

@j6Kg2((('' + ('' + 'sc')) + (('r' + 'een_') + ('wid' + 'th'))))
def cWOG65():
    'GNv1cZ_591ZrSgJ918_bF07'
    return (turtle.getcanvas().winfo_width() // h02_D.M288_O)

@j6Kg2((chr(115) + (('cree' + 'n_heigh') + chr(116))))
def U59rdq1():
    's033py1__k_708448_68Y2l'
    return (turtle.getcanvas().winfo_height() // h02_D.M288_O)
'tE37A3_s5_ACM_4__5_TiWa'
s__1kq_6 = (set(string.digits) | set((('' + ('+' + '-')) + '.')))
G3o5_ = (((set(((('' + '!$') + ('%&*/:<=>?' + '@')) + (chr(94) + ('_' + '~')))) | set(string.ascii_lowercase)) | set(string.ascii_uppercase)) | s__1kq_6)
p978kC = set('"')
lPqI951 = set((chr((-17 + 49)) + (('' + '\t\n') + chr(13))))
y_78 = set((('' + ('(' + ')')) + (('[' + ']') + ("'" + '`'))))
Z0c11K7O = (((lPqI951 | y_78) | p978kC) | {chr(((-2 + 96) + (-82 + 32))), (chr(44) + chr((-32 + 96)))})
cN_3_np = (y_78 | {chr(((-51 + 33) + (-27 + 91))), chr(((51 + 64) + (-93 + 22))), ('' + (',' + '@'))})

def MCy826n(d988):
    'W_hHtt_1n3j2e9SJg34PX9Eb'
    if (len(d988) == int((((-0.2915076839612827 + 0.2740027179952069) + (0.19450747916848743 + 0.3870289323148465)) * int(((0.32774515425660655 + 0.0751810472294755) * 0))))):
        return False
    for yc2mB10t in d988:
        if (yc2mB10t not in G3o5_):
            return False
    return True

def GF49L(u_63615y, Ge_8m8):
    'T_6j7Z6__32XbqHb_85H__M80C7'
    while (Ge_8m8 < len(u_63615y)):
        yc2mB10t = u_63615y[Ge_8m8]
        if (yc2mB10t == chr(((-31 + 65) + (13 + 12)))):
            return (None, len(u_63615y))
        elif (yc2mB10t in lPqI951):
            Ge_8m8 += (((-46 + 76) + (-20 + -37)) + ((153 + -28) + (-28 + -69)))
        elif (yc2mB10t in y_78):
            if (yc2mB10t == chr(((246 + -65) + (-65 + -23)))):
                yc2mB10t = ')'
            if (yc2mB10t == chr(((216 + -64) + (-75 + 14)))):
                yc2mB10t = chr((23 + 17))
            return (yc2mB10t, (Ge_8m8 + (((-62 + 30) + (25 + -80)) + ((108 + 45) + (-45 + -20)))))
        elif (yc2mB10t == chr(((-3 + 34) + (-32 + 36)))):
            return (u_63615y[Ge_8m8:(Ge_8m8 + (((-48 + 31) + (-17 + -20)) + ((3 + 60) + (-84 + 77))))], min((Ge_8m8 + (((-54 + 87) + (-36 + -43)) + ((98 + 17) + (-89 + 22)))), len(u_63615y)))
        elif (yc2mB10t == chr(((8 + -17) + (-26 + 79)))):
            if (((Ge_8m8 + (((-81 + 80) + (-134 + 92)) + ((-148 + 95) + (55 + 42)))) < len(u_63615y)) and (u_63615y[(Ge_8m8 + (((79 + 49) + (31 + -83)) + ((-32 + 57) + (-121 + 21))))] == chr(64))):
                return ((chr((59 + -15)) + chr(64)), (Ge_8m8 + (((39 + 97) + (-42 + -6)) + ((-102 + -24) + (38 + 2)))))
            return (yc2mB10t, (Ge_8m8 + (((70 + 11) + (6 + -34)) + ((52 + -87) + (63 + -80)))))
        elif (yc2mB10t in p978kC):
            if (((Ge_8m8 + (((5 + 37) + (-34 + -43)) + ((95 + -42) + (5 + -22)))) < len(u_63615y)) and (u_63615y[(Ge_8m8 + (((188 + -89) + (49 + -85)) + ((-85 + 43) + (-87 + 67))))] == yc2mB10t)):
                return ((yc2mB10t + yc2mB10t), (Ge_8m8 + (((64 + 50) + (-173 + 75)) + ((6 + -14) + (89 + -95)))))
            E07B3F_L = (bytes(u_63615y[Ge_8m8:], encoding=(str() + (str() + ('u' + 'tf-8')))),)
            Zz_k = tokenize.tokenize(iter(E07B3F_L).__next__)
            next(Zz_k)
            D__Zr61X0 = next(Zz_k)
            if (D__Zr61X0.type != tokenize.STRING):
                raise ValueError(((str() + ('inv' + 'alid ')) + (('str' + 'i') + ('n' + 'g: {0}'))).format(D__Zr61X0.string))
            return (D__Zr61X0.string, (D__Zr61X0.end[(((-66 + 53) + (116 + -28)) + ((-100 + 48) + (-62 + 40)))] + Ge_8m8))
        else:
            ni71__7H4 = Ge_8m8
            while ((ni71__7H4 < len(u_63615y)) and (u_63615y[ni71__7H4] not in Z0c11K7O)):
                ni71__7H4 += (((152 + -70) + (-60 + -11)) + ((24 + -60) + (-68 + 94)))
            return (u_63615y[Ge_8m8:ni71__7H4], min(ni71__7H4, len(u_63615y)))
    return (None, len(u_63615y))

def d10f(u_63615y):
    'ubq5J2_royn1R__8g_wCK7'
    PR61 = []
    (p6o1671_6, v659) = GF49L(u_63615y, int((((-0.8489035085259656 + 0.5159470698725457) + (0.09549062144974318 + 0.4462186844340076)) * int(((-0.0855627032390528 + 0.5774001059728008) * int((0.13596573665660816 * 0)))))))
    while (p6o1671_6 is not None):
        if (p6o1671_6 in cN_3_np):
            PR61.append(p6o1671_6)
        elif ((p6o1671_6 == (str() + ('' + ('#' + 't')))) or (p6o1671_6.lower() == (chr((200 + -84)) + (str() + ('ru' + 'e'))))):
            PR61.append(True)
        elif ((p6o1671_6 == (chr((90 + -55)) + chr((80 + 22)))) or (p6o1671_6.lower() == (chr((131 + -29)) + (('' + 'als') + chr(101))))):
            PR61.append(False)
        elif (p6o1671_6 == ((str() + ('' + 'ni')) + 'l')):
            PR61.append(p6o1671_6)
        elif (p6o1671_6[int((((-1.19840393722241 + 0.9428440318177135) + (0.515938781687467 + 0.12123194713216656)) * int(((0.23080582188213838 + 0.2090570767225044) * 0))))] in G3o5_):
            P_t1ut__9 = False
            if (p6o1671_6[0] in s__1kq_6):
                try:
                    PR61.append(int(p6o1671_6))
                    P_t1ut__9 = True
                except ValueError:
                    try:
                        PR61.append(float(p6o1671_6))
                        P_t1ut__9 = True
                    except ValueError:
                        pass
            if (not P_t1ut__9):
                if MCy826n(p6o1671_6):
                    PR61.append(p6o1671_6.lower())
                else:
                    raise ValueError((('' + ('invali' + 'd numeral o')) + (('r sy' + 'mbol: ') + ('{0' + '}'))).format(p6o1671_6))
        elif (p6o1671_6[int((((-0.8383856443074821 + 0.6338654575639132) + (-0.6733285975196002 + 0.9124211259587609)) * 0))] in p978kC):
            PR61.append(p6o1671_6)
        else:
            print(((('wa' + 'rni') + 'n') + ('g' + (': invalid to' + 'ken: {0}'))).format(p6o1671_6), file=sys.stderr)
            print((str() + (('' + '  ') + ('' + '  '))), u_63615y, file=sys.stderr)
            print((chr((7 + 25)) * (v659 + (((42 + -71) + (50 + -27)) + ((-123 + 33) + (195 + -96))))), chr(((100 + -51) + (82 + -37))), file=sys.stderr)
        (p6o1671_6, v659) = GF49L(u_63615y, v659)
    return PR61

def E93_r3A_N(input):
    'V7Kh8q197f___48X_pWV'
    return map(d10f, input)

def TqB5_17(input):
    'PaKe_T38____R__H5__47454c5X1_'
    return len(list(filter((lambda h0_0U349C: (h0_0U349C not in cN_3_np)), itertools.chain(*E93_r3A_N(input)))))

def YY__LMP_(*W1396B3xw):
    import argparse
    a_S4_J3 = argparse.ArgumentParser(description=(('' + ('Co' + 'u')) + (('nt Schem' + 'e token') + ('' + 's.'))))
    a_S4_J3.add_argument(('' + ('f' + ('il' + 'e'))), nargs=chr((121 + -58)), type=argparse.FileType(chr(((217 + -82) + (-118 + 97)))), default=sys.stdin, help=(('i' + ('np' + 'ut f')) + (('i' + 'le to be c') + ('' + 'ounted'))))
    W1396B3xw = a_S4_J3.parse_args()
    print(((chr(99) + ('' + 'ount')) + ('e' + 'd')), TqB5_17(W1396B3xw.file), (('' + ('non-del' + 'imiter tok')) + (str() + ('e' + 'ns'))))
'nc6_8_a8BV7Z2_D22_Y2mW'
__version__ = ((('' + '1.') + ('' + '2.')) + chr(51))

def zGLT__(By3f_, u7ByO_hb_, Tix5jx2=None):
    'Cs_4607hW1b_qk_7KIk5_2_N3'
    u7ByO_hb_.stack.append(By3f_)
    if G3_91o4(By3f_):
        PR61 = u7ByO_hb_.I0470(By3f_)
        u7ByO_hb_.stack.pop()
        return PR61
    elif i0_5i_(By3f_):
        u7ByO_hb_.stack.pop()
        return By3f_
    if (not nFZ5(By3f_)):
        raise tHw1_52C4((('m' + ('' + 'alformed list:')) + (' ' + ('{' + '0}'))).format(repl_str(By3f_)))
    (p94cc908, R0_0o) = (By3f_.p94cc908, By3f_.U__BH)
    if (G3_91o4(p94cc908) and (p94cc908 in nzpR24954)):
        PR61 = nzpR24954[p94cc908](R0_0o, u7ByO_hb_)
        u7ByO_hb_.stack.pop()
        return PR61
    else:
        R7E_JLdY = zGLT__(p94cc908, u7ByO_hb_)
        fj2F(R7E_JLdY)
        PR61 = R7E_JLdY.o2__(R0_0o, u7ByO_hb_)
        u7ByO_hb_.stack.pop()
        return PR61

def i0_5i_(By3f_):
    'S_58hQpa_H31Iag8_md7'
    return (NvB_k7(By3f_) or L5e__s8GH(By3f_) or (By3f_ is None))

def fxWo1_D(R7E_JLdY, W1396B3xw, u7ByO_hb_):
    'k97T7U79c0G41P8BGYsUq'
    fj2F(R7E_JLdY)
    return R7E_JLdY.dt40S76(W1396B3xw, u7ByO_hb_)

def W_pV1Y(p3pC_, u7ByO_hb_):
    'n30b2cU1Zn8_5_E9GY7z1L_L_79_'
    nWt7_7e = None
    while (p3pC_ is not nil):
        iv_K5 = (p3pC_.U__BH is nil)
        nWt7_7e = zGLT__(p3pC_.p94cc908, u7ByO_hb_, iv_K5)
        p3pC_ = p3pC_.U__BH
    return nWt7_7e

class Ge6_():
    'CC_2VH25_8r_1pQ83BLR4_8_'

    def __init__(Yipzrwt_o, k60O0ar):
        'J7_b9Ju_7A4x58497_Z1x_25d'
        Yipzrwt_o.vp_Xn2N = {}
        Yipzrwt_o.k60O0ar = k60O0ar
        if Yipzrwt_o.k60O0ar:
            Yipzrwt_o.stack = Yipzrwt_o.k60O0ar.stack
        else:
            Yipzrwt_o.stack = []

    def __repr__(Yipzrwt_o):
        if (Yipzrwt_o.k60O0ar is None):
            return ((('' + '<G') + ('' + 'lob')) + (str() + ('' + 'al Frame>')))
        d988 = sorted([(chr(123) + (str() + ('0}:' + ' {1}'))).format(Ge_8m8, EMy9T_pc) for (Ge_8m8, EMy9T_pc) in Yipzrwt_o.vp_Xn2N.items()])
        return ((('<' + '{') + ('{' + '{')) + (('0}' + '}') + ('} -> {' + '1}>'))).format((chr((-46 + 90)) + chr((122 + -90))).join(d988), repr(Yipzrwt_o.k60O0ar))

    def VW9l(Yipzrwt_o, I2g6uh112, nWt7_7e):
        'u854D524_pPWd1u6406540M_AX'
        Yipzrwt_o.vp_Xn2N[I2g6uh112] = nWt7_7e

    def I0470(Yipzrwt_o, I2g6uh112):
        'iyb43V_79957_K_9_0n_cA'
        S8wp3o = Yipzrwt_o
        while (S8wp3o is not None):
            if (I2g6uh112 in S8wp3o.vp_Xn2N):
                return S8wp3o.vp_Xn2N[I2g6uh112]
            S8wp3o = S8wp3o.k60O0ar
        raise tHw1_52C4(((('un' + 'k') + 'n') + (('' + 'own') + (' iden' + 'tifier: {0}'))).format(I2g6uh112))

    def Pd9_5_hz(Yipzrwt_o, I2g6uh112, nWt7_7e):
        'e7k7nB8_160wZEM8_Rwec'
        S8wp3o = Yipzrwt_o
        while (S8wp3o is not None):
            if (I2g6uh112 in S8wp3o.vp_Xn2N):
                S8wp3o.vp_Xn2N[I2g6uh112] = nWt7_7e
                return
            S8wp3o = S8wp3o.k60O0ar
        raise tHw1_52C4(((('' + 'un') + ('known' + ' identifi')) + (str() + ('er: {' + '0}'))).format(I2g6uh112))

    def a97__(Yipzrwt_o, NJ0_Z9, rj_L_8):
        'v1x9iUK66yi33CAbY8qE_o8a_OV_'
        Wg3_WE9 = Ge6_(Yipzrwt_o)
        while isinstance(NJ0_Z9, Pair):
            if (rj_L_8 is nil):
                raise tHw1_52C4(((('too' + ' fe') + ('w ar' + 'guments t')) + (('o fun' + 'c') + ('t' + 'ion call'))))
            Wg3_WE9.VW9l(NJ0_Z9.p94cc908, rj_L_8.p94cc908)
            (NJ0_Z9, rj_L_8) = (NJ0_Z9.U__BH, rj_L_8.U__BH)
        if (NJ0_Z9 != nil):
            Wg3_WE9.VW9l(NJ0_Z9, rj_L_8)
        elif (rj_L_8 != nil):
            raise tHw1_52C4(((chr(116) + ('oo many argument' + 's to function c')) + (str() + ('' + 'all'))))
        return Wg3_WE9

class nI1na4_():
    'tOPL6my6S_M4d73t705sw86xCI__X'

    def o2__(Yipzrwt_o, E0l_, u7ByO_hb_):
        'DW40M5pTPu26Z539k9mOc_Lm63'
        W1396B3xw = E0l_.map((lambda c6O_1MTVr: zGLT__(c6O_1MTVr, u7ByO_hb_)))
        return fxWo1_D(Yipzrwt_o, W1396B3xw, u7ByO_hb_)

def Xa3534(h0_0U349C):
    return isinstance(h0_0U349C, nI1na4_)

class PrimitiveProcedure(nI1na4_):
    'o0se_7AU1a4_8sXs9724'

    def __init__(Yipzrwt_o, LMft4_, X1d_=False, K60___u0='primitive'):
        Yipzrwt_o.K60___u0 = K60___u0
        Yipzrwt_o.LMft4_ = LMft4_
        Yipzrwt_o.X1d_ = X1d_

    def __str__(Yipzrwt_o):
        return ((('' + '#[{') + ('' + '0}')) + chr(93)).format(Yipzrwt_o.K60___u0)

    def dt40S76(Yipzrwt_o, W1396B3xw, u7ByO_hb_):
        'a0___C__pe16p7fC72i99'
        if (not nFZ5(W1396B3xw)):
            raise tHw1_52C4(((('arguments ' + 'are not in a list') + ('' + ': ')) + (str() + ('{0' + '}'))).format(W1396B3xw))
        d7Y904 = []
        while (W1396B3xw is not nil):
            d7Y904.append(W1396B3xw.p94cc908)
            W1396B3xw = W1396B3xw.U__BH
        if Yipzrwt_o.X1d_:
            d7Y904.append(u7ByO_hb_)
        try:
            return Yipzrwt_o.LMft4_(*d7Y904)
        except TypeError as SjS5gc8:
            raise tHw1_52C4((('i' + ('ncorr' + 'ect')) + ((' nu' + 'mber of ') + ('arguments: {0' + '}'))).format(Yipzrwt_o))

class rJW1__Vo(nI1na4_):
    'M01GtA3p00a0KXJ199i2R7a1U'

    def dt40S76(Yipzrwt_o, W1396B3xw, u7ByO_hb_):
        'y__1i8Q30EL7Ee_S394ez'
        P261 = Yipzrwt_o.t15_k51__(W1396B3xw, u7ByO_hb_)
        return W_pV1Y(Yipzrwt_o.Cpr77_p9, P261)

class LambdaProcedure(rJW1__Vo):
    'kY2ycn2_84qUBw_3__Vd_9i645__'
    K60___u0 = ((('[l' + 'amb') + chr(100)) + ('' + ('a' + ']')))

    def __init__(Yipzrwt_o, NJ0_Z9, Cpr77_p9, u7ByO_hb_):
        'vg058x__2WH_93d242_a_lG_3F7'
        Yipzrwt_o.NJ0_Z9 = NJ0_Z9
        Yipzrwt_o.Cpr77_p9 = Cpr77_p9
        Yipzrwt_o.u7ByO_hb_ = u7ByO_hb_

    def t15_k51__(Yipzrwt_o, W1396B3xw, u7ByO_hb_):
        'XQ5hV_Z8_ih62q5000jW7vH44'
        return Yipzrwt_o.u7ByO_hb_.a97__(Yipzrwt_o.NJ0_Z9, W1396B3xw)

    def __str__(Yipzrwt_o):
        return str(Pair((str() + (chr(108) + ('am' + 'bda'))), Pair(Yipzrwt_o.NJ0_Z9, Yipzrwt_o.Cpr77_p9)))

    def __repr__(Yipzrwt_o):
        return ((('L' + 'a') + ('' + 'mbd')) + (('aProcedure({0}, {1' + '}') + (', {2}' + ')'))).format(repr(Yipzrwt_o.NJ0_Z9), repr(Yipzrwt_o.Cpr77_p9), repr(Yipzrwt_o.u7ByO_hb_))

class HR8m6f12(LambdaProcedure):
    'pK8Rj1K6vB_5E2_b04T2_b9N5'

    def o2__(Yipzrwt_o, E0l_, u7ByO_hb_):
        'LK7c_45l_1r6_26667J80137OYM'
        By3f_ = i2H__G(fxWo1_D(Yipzrwt_o, E0l_, u7ByO_hb_))
        return zGLT__(By3f_, u7ByO_hb_)

def mA79m(s3Y9aI_w_, Yx89_k):
    'n_5Cs1_18VH5D_25_6s0p'
    for (K60___u0, LMft4_, nFuTVt71) in Yx89_k:
        s3Y9aI_w_.VW9l(K60___u0, PrimitiveProcedure(LMft4_, K60___u0=nFuTVt71))

def V_28O_(p3pC_, u7ByO_hb_):
    'szj_l812q_175__131s8Y'
    T54VL(p3pC_, (((114 + -10) + (-84 + 77)) + ((-205 + 76) + (82 + -48))))
    tm_y = p3pC_.p94cc908
    if G3_91o4(tm_y):
        T54VL(p3pC_, (((103 + 15) + (-131 + 49)) + ((-75 + -48) + (109 + -20))), (((-195 + 13) + (22 + 66)) + ((97 + 70) + (-99 + 28))))
        nWt7_7e = zGLT__(p3pC_.U__BH.p94cc908, u7ByO_hb_)
        u7ByO_hb_.VW9l(tm_y, nWt7_7e)
        return tm_y
    elif (isinstance(tm_y, Pair) and G3_91o4(tm_y.p94cc908)):
        K60___u0 = tm_y.p94cc908
        NJ0_Z9 = tm_y.U__BH
        Cpr77_p9 = p3pC_.U__BH
        nWt7_7e = FNh07n(Pair(NJ0_Z9, Cpr77_p9), u7ByO_hb_)
        nWt7_7e.K60___u0 = K60___u0
        u7ByO_hb_.VW9l(K60___u0, nWt7_7e)
        return K60___u0
    else:
        Nh511_3 = (tm_y.p94cc908 if isinstance(tm_y, Pair) else tm_y)
        raise tHw1_52C4((('' + ('non-sym' + 'b')) + (str() + ('' + 'ol: {0}'))).format(Nh511_3))

def F_738_(p3pC_, u7ByO_hb_):
    'io_8__1_lW3Rih_X_K7hI04v_e'
    T54VL(p3pC_, (((-89 + -41) + (179 + -79)) + ((-24 + 98) + (-59 + 16))), (((-56 + -51) + (57 + -5)) + ((-7 + 88) + (-44 + 19))))
    return p3pC_.p94cc908

def R58_Q(p3pC_, u7ByO_hb_):
    'q50074_6524s__2Q2Vu2F3'
    T54VL(p3pC_, (((85 + -92) + (-95 + 67)) + ((65 + -68) + (87 + -48))))
    return W_pV1Y(p3pC_, u7ByO_hb_)

def FNh07n(p3pC_, u7ByO_hb_):
    'n_8Y8967ae6_87_Ic9MV8'
    T54VL(p3pC_, (((-188 + 14) + (37 + 61)) + ((1 + -6) + (-16 + 99))))
    NJ0_Z9 = p3pC_.p94cc908
    B7QL5N(NJ0_Z9)
    return LambdaProcedure(NJ0_Z9, p3pC_.U__BH, u7ByO_hb_)

def c9HjT_0bd(p3pC_, u7ByO_hb_):
    'R4282N93_3y4247Mu___3Op_'
    T54VL(p3pC_, (((-75 + 18) + (116 + -27)) + ((-141 + 65) + (-10 + 56))), (((38 + 18) + (15 + -44)) + ((-35 + -76) + (-5 + 92))))
    if b7WA00(zGLT__(p3pC_.p94cc908, u7ByO_hb_)):
        return zGLT__(p3pC_.U__BH.p94cc908, u7ByO_hb_, True)
    elif (len(p3pC_) == (((8 + 23) + (70 + 1)) + ((-41 + -42) + (-12 + -4)))):
        return zGLT__(p3pC_.U__BH.U__BH.p94cc908, u7ByO_hb_, True)

def S_T02yc5N(p3pC_, u7ByO_hb_):
    'S06_30vUTw_dG_W34jd2_wSEqV519'
    nWt7_7e = True
    while (p3pC_ is not nil):
        iv_K5 = (p3pC_.U__BH is nil)
        nWt7_7e = zGLT__(p3pC_.p94cc908, u7ByO_hb_, iv_K5)
        if i_Bv_r0_5(nWt7_7e):
            return nWt7_7e
        p3pC_ = p3pC_.U__BH
    return nWt7_7e

def xPQz(p3pC_, u7ByO_hb_):
    'WugXgNH3W76P_WvpsJ4AT50'
    nWt7_7e = False
    while (p3pC_ is not nil):
        iv_K5 = (p3pC_.U__BH is nil)
        nWt7_7e = zGLT__(p3pC_.p94cc908, u7ByO_hb_, iv_K5)
        if b7WA00(nWt7_7e):
            return nWt7_7e
        p3pC_ = p3pC_.U__BH
    return nWt7_7e

def I_jGBe(p3pC_, u7ByO_hb_):
    'V193e_3U01tzq_6X4_PmtY8PY_P'
    while (p3pC_ is not nil):
        Mo_UDp = p3pC_.p94cc908
        T54VL(Mo_UDp, (((0 + -96) + (50 + 39)) + ((4 + 94) + (-21 + -69))))
        if (Mo_UDp.p94cc908 == (chr((6 + 95)) + (chr(108) + ('s' + 'e')))):
            Wc71_ = True
            if (p3pC_.U__BH != nil):
                raise tHw1_52C4(((('e' + 'ls') + ('e must ' + 'be')) + (('' + ' las') + 't')))
        else:
            Wc71_ = zGLT__(Mo_UDp.p94cc908, u7ByO_hb_)
        if b7WA00(Wc71_):
            if (len(Mo_UDp) == (((15 + 89) + (-20 + 13)) + ((42 + -92) + (-101 + 55)))):
                return Wc71_
            else:
                return W_pV1Y(Mo_UDp.U__BH, u7ByO_hb_)
        p3pC_ = p3pC_.U__BH

def y3u_27X(p3pC_, u7ByO_hb_):
    'T77d1k0I5_xTnCM01_J_2hh2D__'
    T54VL(p3pC_, (((77 + 72) + (-143 + 71)) + ((-53 + -14) + (89 + -97))))
    N_mT4B0z = PCF6W3(p3pC_.p94cc908, u7ByO_hb_)
    return W_pV1Y(p3pC_.U__BH, N_mT4B0z)

def PCF6W3(vp_Xn2N, u7ByO_hb_):
    'KtZC3xp6__h1g1_0BCl1'
    if (not nFZ5(vp_Xn2N)):
        raise tHw1_52C4(((chr(98) + ('ad b' + 'indi')) + (('ngs l' + 'i') + ('st i' + 'n let form'))))
    (YglxiK8HA, Id_9A70Q) = (nil, nil)
    while (vp_Xn2N is not nil):
        GL9l017_ = vp_Xn2N.p94cc908
        T54VL(GL9l017_, (((-3 + -97) + (50 + -23)) + ((-19 + 94) + 0)), (((-15 + 93) + (4 + -88)) + ((63 + 19) + (-75 + 1))))
        K60___u0 = GL9l017_.p94cc908
        t_p8_4c0 = zGLT__(GL9l017_.U__BH.p94cc908, u7ByO_hb_)
        YglxiK8HA = Pair(K60___u0, YglxiK8HA)
        Id_9A70Q = Pair(t_p8_4c0, Id_9A70Q)
        vp_Xn2N = vp_Xn2N.U__BH
    B7QL5N(YglxiK8HA)
    return u7ByO_hb_.a97__(YglxiK8HA, Id_9A70Q)

def hV8_81(p3pC_, u7ByO_hb_):
    'kj7R9S3M_W4V83Csch382_u3__71'
    T54VL(p3pC_, (((65 + -49) + (45 + -35)) + ((60 + -76) + (-69 + 61))))
    tm_y = p3pC_.p94cc908
    if (isinstance(tm_y, Pair) and G3_91o4(tm_y.p94cc908)):
        K60___u0 = tm_y.p94cc908
        NJ0_Z9 = tm_y.U__BH
        Cpr77_p9 = p3pC_.U__BH
        B7QL5N(NJ0_Z9)
        nWt7_7e = HR8m6f12(NJ0_Z9, Cpr77_p9, u7ByO_hb_)
        nWt7_7e.K60___u0 = K60___u0
        u7ByO_hb_.VW9l(K60___u0, nWt7_7e)
        return K60___u0
    else:
        raise tHw1_52C4(('' + (('improper' + ' form') + (' for d' + 'efine-macro'))))

def Xj_i_(p3pC_, u7ByO_hb_):
    'Q57_66q07g16T14uqv2K_4'
    T54VL(p3pC_, (((116 + -92) + (-123 + 54)) + ((41 + 87) + (-122 + 41))))
    K60___u0 = p3pC_.p94cc908
    if (not G3_91o4(K60___u0)):
        raise tHw1_52C4((((chr(98) + chr(97)) + (('d ar' + 'gum') + ('e' + 'nt: '))) + repl_str(K60___u0)))
    nWt7_7e = zGLT__(p3pC_.U__BH.p94cc908, u7ByO_hb_)
    u7ByO_hb_.Pd9_5_hz(K60___u0, nWt7_7e)

def LhbMl7(p3pC_, u7ByO_hb_):
    'Zd0B8s03U_9_8_5vY_0Ba96'
    T54VL(p3pC_, (((104 + -79) + (28 + 7)) + ((-93 + 14) + (33 + -13))), (((37 + 47) + (-150 + 83)) + ((-26 + 83) + (-120 + 47))))
    (t_p8_4c0, m3O9Wk) = oQCIW(p3pC_.p94cc908, u7ByO_hb_)
    if m3O9Wk:
        E5OO0GPSw = ((('u' + 'nq') + ('' + 'uo')) + (('' + 'te-') + ('splici' + 'ng not in list template: {0}')))
        raise tHw1_52C4(E5OO0GPSw.format(p3pC_.p94cc908))
    return t_p8_4c0

def oQCIW(t_p8_4c0, u7ByO_hb_, gx22604z0=1):
    'iD95527_38_3__B_6_1j2__5_5_0'
    if H3pGJGl(t_p8_4c0):
        if (t_p8_4c0.p94cc908 in (((('un' + 'q') + 'u') + (('' + 'ot') + chr(101))), ((('u' + 'n') + ('' + 'qu')) + ('' + ('ote-' + 'splicing'))))):
            gx22604z0 -= (((-76 + 79) + (32 + 9)) + ((94 + -57) + (-124 + 44)))
            if (gx22604z0 == 0):
                p3pC_ = t_p8_4c0.U__BH
                T54VL(p3pC_, (((50 + 16) + (78 + -94)) + (int((0.005711928689976387 * 0)) + (-73 + 24))), (((183 + -97) + (-24 + -9)) + ((-26 + -90) + (114 + -50))))
                jB_dVB14 = zGLT__(p3pC_.p94cc908, u7ByO_hb_)
                m3O9Wk = (t_p8_4c0.p94cc908 == (str() + (('' + 'unquo') + ('te-splici' + 'ng'))))
                if (m3O9Wk and (not nFZ5(jB_dVB14))):
                    E5OO0GPSw = ((('u' + 'nquo') + ('te-splici' + 'ng used on')) + (('' + ' non') + ('-lis' + 't: {0}')))
                    raise tHw1_52C4(E5OO0GPSw.format(jB_dVB14))
                return (jB_dVB14, m3O9Wk)
        elif (t_p8_4c0.p94cc908 == ((('qu' + 'asi') + 'q') + (('' + 'uot') + chr(101)))):
            gx22604z0 += (((-38 + 82) + (18 + -72)) + ((-4 + 28) + (14 + -27)))
        (p94cc908, m3O9Wk) = oQCIW(t_p8_4c0.p94cc908, u7ByO_hb_, gx22604z0)
        (U__BH, Tix5jx2) = oQCIW(t_p8_4c0.U__BH, u7ByO_hb_, gx22604z0)
        if m3O9Wk:
            if (U__BH is not nil):
                return (izgR11K_n(p94cc908, U__BH), False)
            return (p94cc908, False)
        return (Pair(p94cc908, U__BH), False)
    else:
        return (t_p8_4c0, False)

def PV6Y2u4i(p3pC_, u7ByO_hb_):
    raise tHw1_52C4(((('un' + 'q') + ('uote outsi' + 'd')) + (('e' + ' of qu') + ('' + 'asiquote'))))
nzpR24954 = {(chr(97) + (chr(110) + 'd')): S_T02yc5N, ((str() + ('b' + 'egi')) + 'n'): R58_Q, (chr(99) + ('' + ('o' + 'nd'))): I_jGBe, ((('d' + 'e') + 'f') + (('' + 'in') + chr(101))): V_28O_, ('i' + chr(102)): c9HjT_0bd, (chr((179 + -71)) + (str() + ('amb' + 'da'))): FNh07n, (('' + ('l' + 'e')) + chr(116)): y3u_27X, (str() + (str() + ('' + 'or'))): xPQz, ('' + (('' + 'quo') + ('' + 'te'))): F_738_, (('' + ('d' + 'ef')) + (('in' + 'e') + ('-ma' + 'cro'))): hV8_81, (str() + ('' + ('' + 'set!'))): Xj_i_, (('q' + ('ua' + 'si')) + (('qu' + 'o') + ('t' + 'e'))): LhbMl7, ('u' + ('' + ('' + 'nquote'))): PV6Y2u4i, (('u' + ('nquo' + 'te-splici')) + (chr(110) + 'g')): PV6Y2u4i}

def T54VL(By3f_, min, max=float('inf')):
    'j22Fz_7_7XSfx_k4m0i0_'
    if (not nFZ5(By3f_)):
        raise tHw1_52C4((((('ba' + 'dly for') + ('med ' + 'e')) + ('' + ('xpres' + 'sion: '))) + repl_str(By3f_)))
    GJ_f = len(By3f_)
    if (GJ_f < min):
        raise tHw1_52C4(((('too f' + 'ew ') + ('operands i' + 'n')) + (('' + ' f') + ('o' + 'rm'))))
    elif (GJ_f > max):
        raise tHw1_52C4(((('too many' + ' ') + ('operands in ' + 'f')) + ('o' + ('r' + 'm'))))

def B7QL5N(NJ0_Z9):
    'sT_h6v__bcT4wEnN10x_M'
    T7_n = set()

    def HVg58Yd(I2g6uh112):
        if (not G3_91o4(I2g6uh112)):
            raise tHw1_52C4((str() + (('no' + 'n-') + ('symb' + 'ol: {0}'))).format(I2g6uh112))
        if (I2g6uh112 in T7_n):
            raise tHw1_52C4(((('d' + 'u') + ('pl' + 'ica')) + (('te symbol: ' + '{0') + chr(125))).format(I2g6uh112))
        T7_n.add(I2g6uh112)
    while isinstance(NJ0_Z9, Pair):
        HVg58Yd(NJ0_Z9.p94cc908)
        NJ0_Z9 = NJ0_Z9.U__BH
    if (NJ0_Z9 != nil):
        HVg58Yd(NJ0_Z9)

def fj2F(R7E_JLdY):
    'z9e8p1_4_9vS2_84200P_7_4V8p'
    if (not Xa3534(R7E_JLdY)):
        raise tHw1_52C4(((('{' + '0}') + (' ' + 'is not callable: {')) + (chr(49) + '}')).format(type(R7E_JLdY).__name__.lower(), repl_str(R7E_JLdY)))

class MuProcedure(rJW1__Vo):
    'K5_x739dc__3C_0t5zZ_'
    K60___u0 = (str() + ('' + ('[mu' + ']')))

    def __init__(Yipzrwt_o, NJ0_Z9, Cpr77_p9):
        'r301_6Us2f__R8A5393_V7_1'
        Yipzrwt_o.NJ0_Z9 = NJ0_Z9
        Yipzrwt_o.Cpr77_p9 = Cpr77_p9

    def t15_k51__(Yipzrwt_o, W1396B3xw, u7ByO_hb_):
        'U3_V40Oil312_f7T24n_O82oS69_u'
        return u7ByO_hb_.a97__(Yipzrwt_o.NJ0_Z9, W1396B3xw)

    def __str__(Yipzrwt_o):
        return str(Pair((chr((105 + 4)) + chr(117)), Pair(Yipzrwt_o.NJ0_Z9, Yipzrwt_o.Cpr77_p9)))

    def __repr__(Yipzrwt_o):
        return ((chr(77) + ('u' + 'Pr')) + (('ocedure({0' + '},') + (' {' + '1})'))).format(repr(Yipzrwt_o.NJ0_Z9), repr(Yipzrwt_o.Cpr77_p9))

def s_yve_(p3pC_, u7ByO_hb_):
    'k_Mu350_Ti_CiD90678bW8'
    T54VL(p3pC_, (((-36 + 59) + (145 + -95)) + ((-113 + -17) + (2 + 57))))
    NJ0_Z9 = p3pC_.p94cc908
    B7QL5N(NJ0_Z9)
    return MuProcedure(NJ0_Z9, p3pC_.U__BH)
nzpR24954[(str() + (str() + ('m' + 'u')))] = s_yve_

class Promise():
    'i5EV_u_8b0dTK57s9F9K5l'

    def __init__(Yipzrwt_o, el1x0491, u7ByO_hb_):
        Yipzrwt_o.el1x0491 = el1x0491
        Yipzrwt_o.u7ByO_hb_ = u7ByO_hb_

    def M_0R0_(Yipzrwt_o):
        if (Yipzrwt_o.el1x0491 is not None):
            Yipzrwt_o.nWt7_7e = zGLT__(Yipzrwt_o.el1x0491, Yipzrwt_o.u7ByO_hb_.a97__(nil, nil))
            Yipzrwt_o.el1x0491 = None
        return Yipzrwt_o.nWt7_7e

    def __str__(Yipzrwt_o):
        return ((('#[promise' + ' ({0}') + ('forc' + 'e')) + ('d' + ('' + ')]'))).format(((str() + (('no' + 't') + ' ')) if (Yipzrwt_o.el1x0491 is not None) else str()))

def ORKi58s1B(p3pC_, u7ByO_hb_):
    'e85___553f5__88_e_Z0kcm0'
    T54VL(p3pC_, (((202 + -76) + (-124 + 61)) + ((-148 + 42) + (122 + -78))), (((184 + -57) + (-37 + -47)) + ((49 + -94) + (4 + -1))))
    return Promise(p3pC_.p94cc908, u7ByO_hb_)

def m6V_j54_(p3pC_, u7ByO_hb_):
    'L8__ut32_35_Y26_0d7c_l__73B_2'
    T54VL(p3pC_, (((-92 + 99) + (39 + -70)) + ((64 + -20) + (54 + -72))), (((-19 + -88) + (-36 + 48)) + ((22 + 91) + (43 + -59))))
    return Pair(zGLT__(p3pC_.p94cc908, u7ByO_hb_), ORKi58s1B(p3pC_.U__BH, u7ByO_hb_))
nzpR24954[((chr(99) + ('on' + 's')) + (('-s' + 'tre') + ('a' + 'm')))] = m6V_j54_
nzpR24954[((str() + ('d' + 'e')) + (chr(108) + ('a' + 'y')))] = ORKi58s1B

class gU1Ja1u8():
    'y35XEFYg8_Nu1L2q7_V_u'

    def __init__(Yipzrwt_o, By3f_, u7ByO_hb_):
        Yipzrwt_o.By3f_ = By3f_
        Yipzrwt_o.u7ByO_hb_ = u7ByO_hb_

def i2H__G(t_p8_4c0):
    'x_aG14_9KQJd_IV_euVt8'
    if isinstance(t_p8_4c0, gU1Ja1u8):
        return zGLT__(t_p8_4c0.By3f_, t_p8_4c0.u7ByO_hb_)
    else:
        return t_p8_4c0

def K103wq9p(By3f_, u7ByO_hb_, iv_K5=False):
    'Q_8__75Z4QH05dL_6_47_k8'
    u7ByO_hb_.stack.append(By3f_)
    if G3_91o4(By3f_):
        PR61 = u7ByO_hb_.I0470(By3f_)
        u7ByO_hb_.stack.pop()
        return PR61
    elif i0_5i_(By3f_):
        u7ByO_hb_.stack.pop()
        return By3f_
    u7ByO_hb_.stack.pop()
    X_54PnSx3 = len(u7ByO_hb_.stack)
    if iv_K5:
        return gU1Ja1u8(By3f_, u7ByO_hb_)
    else:
        PR61 = gU1Ja1u8(By3f_, u7ByO_hb_)
    while isinstance(PR61, gU1Ja1u8):
        (By3f_, u7ByO_hb_) = (PR61.By3f_, PR61.u7ByO_hb_)
        u7ByO_hb_.stack.append(By3f_)
        if (not nFZ5(By3f_)):
            raise tHw1_52C4(((('ma' + 'lformed') + (' ' + 'l')) + (('ist' + ': {0') + '}')).format(repl_str(By3f_)))
        (p94cc908, R0_0o) = (By3f_.p94cc908, By3f_.U__BH)
        if (G3_91o4(p94cc908) and (p94cc908 in nzpR24954)):
            PR61 = nzpR24954[p94cc908](R0_0o, u7ByO_hb_)
        else:
            R7E_JLdY = zGLT__(p94cc908, u7ByO_hb_)
            fj2F(R7E_JLdY)
            PR61 = R7E_JLdY.o2__(R0_0o, u7ByO_hb_)
    u7ByO_hb_.stack[:] = u7ByO_hb_.stack[:X_54PnSx3]
    return PR61
# zGLT__ = K103wq9p  # TODO: RE-ENABLE TAIL RECURSION, *MAYBE*

def PJ_1(LMft4_, VR0rE4__, u7ByO_hb_):
    cBQ_4(LMft4_, Xa3534, int(((0.2791915891049712 + 0.6729326907324024) * int((0.3426147669936088 * 0)))), (chr((69 + 40)) + ('a' + 'p')))
    cBQ_4(VR0rE4__, nFZ5, (((155 + -41) + (-24 + -66)) + ((-133 + 10) + (169 + -69))), (str() + (chr(109) + ('a' + 'p'))))
    return VR0rE4__.map((lambda h0_0U349C: i2H__G(LMft4_.dt40S76(Pair(h0_0U349C, nil), u7ByO_hb_))))

def wN791w(LMft4_, VR0rE4__, u7ByO_hb_):
    cBQ_4(LMft4_, Xa3534, int(((-0.5988289520613014 + 0.7621149572906756) * 0)), (str() + (('f' + 'il') + ('te' + 'r'))))
    cBQ_4(VR0rE4__, nFZ5, (((12 + 67) + (-8 + -25)) + ((-27 + -47) + (-19 + 48))), (('' + ('' + 'fil')) + (str() + ('' + 'ter'))))
    (g89_2F, current) = (nil, nil)
    while (VR0rE4__ is not nil):
        (NnK6RgOV, VR0rE4__) = (VR0rE4__.p94cc908, VR0rE4__.U__BH)
        if i2H__G(LMft4_.dt40S76(Pair(NnK6RgOV, nil), u7ByO_hb_)):
            if (g89_2F is nil):
                g89_2F = Pair(NnK6RgOV, nil)
                current = g89_2F
            else:
                current.U__BH = Pair(NnK6RgOV, nil)
                current = current.U__BH
    return g89_2F

def E7w38P2(LMft4_, VR0rE4__, u7ByO_hb_):
    cBQ_4(LMft4_, Xa3534, int(((0.18110248679044783 + 0.646228191624571) * int((0.8158053048673091 * 0)))), (('' + ('' + 'red')) + (str() + ('' + 'uce'))))
    cBQ_4(VR0rE4__, (lambda h0_0U349C: (h0_0U349C is not nil)), (((151 + -88) + (-84 + 83)) + ((-182 + 87) + (64 + -30))), (chr(114) + ('' + ('edu' + 'ce'))))
    cBQ_4(VR0rE4__, nFZ5, (((37 + -23) + (-24 + -42)) + ((35 + -56) + (-4 + 78))), (('r' + ('' + 'ed')) + (('' + 'uc') + 'e')))
    (nWt7_7e, VR0rE4__) = (VR0rE4__.p94cc908, VR0rE4__.U__BH)
    while (VR0rE4__ is not nil):
        nWt7_7e = i2H__G(LMft4_.dt40S76(wq8_(nWt7_7e, VR0rE4__.p94cc908), u7ByO_hb_))
        VR0rE4__ = VR0rE4__.U__BH
    return nWt7_7e

def P3o_y4ooX(x3f_w, u7ByO_hb_, j_84f34m=False, W87j1=False, aaf_4F37R=False, zX3m=()):
    'F_S074VS305zDd30_K1s'
    if aaf_4F37R:
        try:
            PVx23liN_((chr((183 + -68)) + (('che' + 'm') + ('' + 'e_lib'))), True, u7ByO_hb_)
        except tHw1_52C4:
            pass
        for Y410yY in zX3m:
            PVx23liN_(Y410yY, True, u7ByO_hb_)
    while True:
        try:
            u722nW_0 = x3f_w()
            while u722nW_0.OQFm:
                el1x0491 = H_5yXx_(u722nW_0)
                PR61 = zGLT__(el1x0491, u7ByO_hb_)
                if ((not W87j1) and (PR61 is not None)):
                    print(repl_str(PR61))
        except (tHw1_52C4, SyntaxError, ValueError, RuntimeError) as SjS5gc8:
            jv28_78(u7ByO_hb_)
            if (isinstance(SjS5gc8, RuntimeError) and (((('' + 'ma') + chr(120)) + (('im' + 'um rec') + ('' + 'ursion depth exceeded'))) not in getattr(SjS5gc8, (chr((59 + 38)) + (str() + ('rg' + 's'))))[int((((0.11412511412637882 + 0.02350112043288355) + (-0.47236854674716766 + 0.7370604328144982)) * int(((0.25000975587599106 + 0.14213235091293674) * 0))))])):
                raise
            elif isinstance(SjS5gc8, RuntimeError):
                print(((('' + 'Error:') + (' maximum recursion depth exc' + 'e')) + (str() + ('' + 'eded'))))
            else:
                print(((('E' + 'r') + 'r') + (('o' + 'r') + chr(58))), SjS5gc8)
        except KeyboardInterrupt:
            if (not aaf_4F37R):
                raise
            u7ByO_hb_.stack = []
            print()
            print((('K' + ('eyboardInterru' + 'p')) + 't'))
            if (not j_84f34m):
                return
        except EOFError:
            print()
            return
E1i7bDtw1 = {(str() + ('' + ('s' + 'et'))): ('' + (str() + ('set' + '!')))}

def jv28_78(u7ByO_hb_):
    print(((('T' + 'r') + ('aceba' + 'ck (most recen')) + (('t ca' + 'll l') + ('as' + 't):'))))
    for (f898u99T, By3f_) in enumerate(u7ByO_hb_.stack):
        print(((chr(32) + ' ') + str(f898u99T)), repl_str(By3f_), sep=chr(9))
    u7ByO_hb_.stack[:] = []

def PVx23liN_(*W1396B3xw):
    'tzK0_28WA5C142U3r1J60A6K_a'
    if (not ((((-51 + -37) + (4 + 12)) + ((109 + -54) + (84 + -65))) <= len(W1396B3xw) <= (((-124 + 94) + (-69 + 97)) + ((-143 + 93) + (-24 + 79))))):
        p3pC_ = W1396B3xw[:(- (((123 + -82) + (33 + -86)) + ((38 + 39) + (-141 + 77))))]
        raise tHw1_52C4(((('"load" given inc' + 'o') + ('rrec' + 't n')) + (('umber of ' + 'ar') + ('guments: ' + '{0}'))).format(len(p3pC_)))
    R1w9 = W1396B3xw[int((((0.06719712899667218 + 0.12334274099017628) + (-0.22880266489489887 + 0.44546854360836685)) * int(((0.42563881052467634 + 0.33120156750172824) * int((0.9215692907482572 * 0))))))]
    W87j1 = (W1396B3xw[(((55 + -12) + (123 + -98)) + ((30 + -79) + (51 + -69)))] if (len(W1396B3xw) > (((-103 + 99) + (-70 + 51)) + ((-63 + 26) + (15 + 47)))) else True)
    u7ByO_hb_ = W1396B3xw[(- (((-86 + 63) + (-69 + -6)) + ((101 + 69) + (-53 + -18))))]
    if L5e__s8GH(R1w9):
        R1w9 = eval(R1w9)
    cBQ_4(R1w9, G3_91o4, int((((-0.18083282500769293 + 0.7872529829510866) + (0.016163452856597482 + 0.11712055904984964)) * int(((0.2721757524633124 + 0.4135399075230387) * int((0.6717501552866518 * 0)))))), (str() + ('l' + ('o' + 'ad'))))
    with AAia51(R1w9) as F_yp:
        xi2_097 = F_yp.readlines()
    W1396B3xw = ((xi2_097, None) if W87j1 else (xi2_097,))

    def x3f_w():
        return Zy_Q3(*W1396B3xw)
    J_25AtW39 = u7ByO_hb_.stack[:]
    u7ByO_hb_.stack[:] = []
    P3o_y4ooX(x3f_w, u7ByO_hb_, W87j1=W87j1)
    u7ByO_hb_.stack[:] = J_25AtW39

def AAia51(Y410yY):
    'w__g3_47u6Ct6__xn_gDe_'
    try:
        return open(Y410yY)
    except IOError as U1_fu6q13:
        if Y410yY.endswith((str() + ('' + ('' + '.scm')))):
            raise tHw1_52C4(str(U1_fu6q13))
    try:
        return open((Y410yY + ('' + ('.' + ('sc' + 'm')))))
    except IOError as U1_fu6q13:
        raise tHw1_52C4(str(U1_fu6q13))

def Y6__():
    'a__g32__2uY4f184K7MO'
    u7ByO_hb_ = Ge6_(None)
    u7ByO_hb_.VW9l((chr((46 + 55)) + ('v' + ('a' + 'l'))), PrimitiveProcedure(zGLT__, True, ((chr(101) + chr(118)) + (chr(97) + 'l'))))
    u7ByO_hb_.VW9l((('' + ('a' + 'ppl')) + chr((35 + 86))), PrimitiveProcedure(fxWo1_D, True, (chr(97) + (('pp' + 'l') + 'y'))))
    u7ByO_hb_.VW9l((('' + ('' + 'lo')) + (str() + ('' + 'ad'))), PrimitiveProcedure(PVx23liN_, True, (str() + (('' + 'loa') + 'd'))))
    u7ByO_hb_.VW9l(((('' + 'pr') + ('oced' + 'u')) + (('' + 're') + '?')), PrimitiveProcedure(Xa3534, False, (str() + (('p' + 'r') + ('ocedure' + '?')))))
    u7ByO_hb_.VW9l((('' + ('m' + 'a')) + chr((103 + 9))), PrimitiveProcedure(PJ_1, True, (str() + (str() + ('' + 'map')))))
    u7ByO_hb_.VW9l(((('fi' + 'l') + chr(116)) + (str() + ('' + 'er'))), PrimitiveProcedure(wN791w, True, ((chr(102) + chr(105)) + (chr(108) + ('' + 'ter')))))
    u7ByO_hb_.VW9l((str() + (chr(114) + ('edu' + 'ce'))), PrimitiveProcedure(E7w38P2, True, ((('' + 'red') + chr(117)) + (chr(99) + chr(101)))))
    u7ByO_hb_.VW9l((chr((197 + -80)) + (('' + 'ndefi') + ('n' + 'ed'))), None)
    u7ByO_hb_.stack = []
    mA79m(u7ByO_hb_, L__2d69)
    return u7ByO_hb_

def YY__LMP_(*argv):
    import argparse
    a_S4_J3 = argparse.ArgumentParser(description=((('CS 61A Sc' + 'heme') + ('' + ' Interp')) + ('' + ('r' + 'eter'))))
    import __main__
    if ((chr((86 + 22)) + ('o' + ('gi' + 'c'))) in __main__.__file__):
        apWO = (str() + (chr(76) + ('ogi' + 'c')))
    else:
        apWO = ((str() + ('S' + 'ch')) + (str() + ('em' + 'e')))
    version = __main__.__version__
    a_S4_J3.add_argument((str() + (chr(45) + ('-versio' + 'n'))), action=(('v' + ('e' + 'r')) + (str() + ('s' + 'ion'))), version=('{' + '}').format(version))
    a_S4_J3.add_argument((str() + ('-' + ('lo' + 'ad'))), (str() + (str() + ('-' + 'i'))), action=(('s' + 't') + (('ore' + '_t') + ('r' + 'ue'))), help=(('' + ('r' + 'un')) + ((' fil' + 'e interactive') + ('' + 'ly'))))
    a_S4_J3.add_argument((chr((75 + 27)) + ('' + ('i' + 'le'))), nargs=chr(((-4 + 85) + (-26 + 8))), type=argparse.FileType(chr(((139 + 10) + (12 + -47)))), default=None, help=(('S' + ('' + 'cheme f')) + (str() + ('ile ' + 'to run'))))
    W1396B3xw = a_S4_J3.parse_args()
    x3f_w = S0G98Hy
    j_84f34m = True
    zX3m = []
    if (W1396B3xw.file is not None):
        if W1396B3xw.load:
            zX3m.append(getattr(W1396B3xw.file, ('n' + (chr(97) + ('m' + 'e')))))
        else:
            xi2_097 = W1396B3xw.file.readlines()

            def x3f_w():
                return Zy_Q3(xi2_097)
            j_84f34m = False
    print(((('We' + 'lcome to the CS 61A ') + ('{} Interpret' + 'er ')) + (('(ve' + 'rsion') + (' {' + '})'))).format(apWO, version))
    P3o_y4ooX(x3f_w, Y6__(), aaf_4F37R=True, j_84f34m=j_84f34m, zX3m=zX3m)
    U_3r30()

