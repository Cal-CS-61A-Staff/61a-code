var $module = (function($B){

var _b_ = $B.builtins,
    $s = [],
    i
for(var $b in _b_){$s.push('var ' + $b +' = _b_["'+$b+'"]')}
eval($s.join(';'))

//for(var $py_builtin in _b_){eval("var "+$py_builtin+"=_b_[$py_builtin]")}

var float_check = function(x) {
    if(x.__class__ === $B.long_int){return parseInt(x.value)}
    return _b_.float.$factory(x)
}

var isWholeNumber = function(x){return (x * 10) % 10 == 0}

var isOdd = function(x) {return isWholeNumber(x) && 2 * Math.floor(x / 2) != x}

var isLargeNumber = function(x) {return x > Math.pow(2, 32)}

// Big number Library from jsfromhell.com
// This library helps with producing "correct" results from
// mathematic operations

//+ Jonas Raoni Soares Silva
//@ http://jsfromhell.com/classes/bignumber [rev. #4]


var BigNumber = function(n, p, r){
    var o = this, i
    if(n instanceof BigNumber){
        for(i in {precision: 0, roundType: 0, _s: 0, _f: 0}){o[i] = n[i]}
        o._d = n._d.slice()
        return
    }
    o.precision = isNaN(p = Math.abs(p)) ? BigNumber.defaultPrecision : p
    o.roundType = isNaN(r = Math.abs(r)) ? BigNumber.defaultRoundType : r
    o._s = (n += "").charAt(0) == "-"
    o._f = ((n = n.replace(/[^\d.]/g, "").split(".", 2))[0] =
        n[0].replace(/^0+/, "") || "0").length
    for(i = (n = o._d = (n.join("") || "0").split("")).length; i;
        n[--i] = +n[i]){}
    o.round()
}
with({$: BigNumber, o: BigNumber.prototype}){
    $.ROUND_HALF_EVEN = ($.ROUND_HALF_DOWN = ($.ROUND_HALF_UP =
        ($.ROUND_FLOOR = ($.ROUND_CEIL = ($.ROUND_DOWN = ($.ROUND_UP = 0) + 1) +
            1) + 1) + 1) + 1) + 1
    $.defaultPrecision = 40
    $.defaultRoundType = $.ROUND_HALF_UP
    o.add = function(n){
        if(this._s != (n = new BigNumber(n))._s){
            return n._s ^= 1, this.subtract(n)
        }
        var o = new BigNumber(this),
            a = o._d,
            b = n._d,
            la = o._f,
            lb = n._f,
            n = Math.max(la, lb),
            i,
            r
        la != lb && ((lb = la - lb) > 0 ? o._zeroes(b, lb, 1) :
            o._zeroes(a, -lb, 1))
        i = (la = a.length) == (lb = b.length) ? a.length :
            ((lb = la - lb) > 0 ? o._zeroes(b, lb) : o._zeroes(a, -lb)).length
        for(r = 0; i; r = (a[--i] = a[i] + b[i] + r) / 10 >>> 0, a[i] %= 10){}
        return r && ++n && a.unshift(r), o._f = n, o.round()
    };
    o.subtract = function(n){
        if(this._s != (n = new BigNumber(n))._s)
            return n._s ^= 1, this.add(n);
        var o = new BigNumber(this),
            c = o.abs().compare(n.abs()) + 1,
            a = c ? o : n,
            b = c ? n : o,
            la = a._f,
            lb = b._f,
            d = la,
            i,
            j;
        a = a._d, b = b._d, la != lb && ((lb = la - lb) > 0 ? o._zeroes(b, lb, 1) : o._zeroes(a, -lb, 1));
        for(i = (la = a.length) == (lb = b.length) ? a.length : ((lb = la - lb) > 0 ? o._zeroes(b, lb) : o._zeroes(a, -lb)).length; i;){
            if(a[--i] < b[i]){
                for(j = i; j && !a[--j]; a[j] = 9);
                --a[j], a[i] += 10;
            }
            b[i] = a[i] - b[i];
        }
        return c || (o._s ^= 1), o._f = d, o._d = b, o.round();
    };
    o.multiply = function(n){
        var o = new BigNumber(this), r = o._d.length >= (n = new BigNumber(n))._d.length, a = (r ? o : n)._d,
        b = (r ? n : o)._d, la = a.length, lb = b.length, x = new BigNumber, i, j, s;
        for(i = lb; i; r && s.unshift(r), x.set(x.add(new BigNumber(s.join("")))))
            for(s = (new Array(lb - --i)).join("0").split(""), r = 0, j = la; j; r += a[--j] * b[i], s.unshift(r % 10), r = (r / 10) >>> 0);
        return o._s = o._s != n._s, o._f = ((r = la + lb - o._f - n._f) >= (j = (o._d = x._d).length) ? this._zeroes(o._d, r - j + 1, 1).length : j) - r, o.round();
    };
    o.divide = function(n){
        if((n = new BigNumber(n)) == "0")
            throw new Error("Division by 0");
        else if(this == "0")
            return new BigNumber;
        var o = new BigNumber(this), a = o._d, b = n._d, la = a.length - o._f,
        lb = b.length - n._f, r = new BigNumber, i = 0, j, s, l, f = 1, c = 0, e = 0;
        r._s = o._s != n._s, r.precision = Math.max(o.precision, n.precision),
        r._f = +r._d.pop(), la != lb && o._zeroes(la > lb ? b : a, Math.abs(la - lb));
        n._f = b.length, b = n, b._s = false, b = b.round();
        for(n = new BigNumber; a[0] == "0"; a.shift());
        out:
        do{
            for(l = c = 0, n == "0" && (n._d = [], n._f = 0); i < a.length && n.compare(b) == -1; ++i){
                (l = i + 1 == a.length, (!f && ++c > 1 || (e = l && n == "0" && a[i] == "0")))
                && (r._f == r._d.length && ++r._f, r._d.push(0));
                (a[i] == "0" && n == "0") || (n._d.push(a[i]), ++n._f);
                if(e)
                    break out;
                if((l && n.compare(b) == -1 && (r._f == r._d.length && ++r._f, 1)) || (l = 0))
                    while(r._d.push(0), n._d.push(0), ++n._f, n.compare(b) == -1);
            }
            if(f = 0, n.compare(b) == -1 && !(l = 0))
                while(l ? r._d.push(0) : l = 1, n._d.push(0), ++n._f, n.compare(b) == -1);
            for(s = new BigNumber, j = 0; n.compare(y = s.add(b)) + 1 && ++j; s.set(y));
            n.set(n.subtract(s)), !l && r._f == r._d.length && ++r._f, r._d.push(j);
        }
        while((i < a.length || n != "0") && (r._d.length - r._f) <= r.precision);
        return r.round();
    };
    o.mod = function(n){
        return this.subtract(this.divide(n).intPart().multiply(n));
    };
    o.pow = function(n){
        var o = new BigNumber(this), i;
        if((n = (new BigNumber(n)).intPart()) == 0) return o.set(1);
        for(i = Math.abs(n); --i; o.set(o.multiply(this)));
        return n < 0 ? o.set((new BigNumber(1)).divide(o)) : o;
    };
    o.set = function(n){
        return this.constructor(n), this;
    };
    o.compare = function(n){
        var a = this, la = this._f, b = new BigNumber(n), lb = b._f, r = [-1, 1], i, l;
        if(a._s != b._s)
            return a._s ? -1 : 1;
        if(la != lb)
            return r[(la > lb) ^ a._s];
        for(la = (a = a._d).length, lb = (b = b._d).length, i = -1, l = Math.min(la, lb); ++i < l;)
            if(a[i] != b[i])
                return r[(a[i] > b[i]) ^ a._s];
        return la != lb ? r[(la > lb) ^ a._s] : 0;
    };
    o.negate = function(){
        var n = new BigNumber(this); return n._s ^= 1, n;
    };
    o.abs = function(){
        var n = new BigNumber(this); return n._s = 0, n;
    };
    o.intPart = function(){
        return new BigNumber((this._s ? "-" : "") + (this._d.slice(0, this._f).join("") || "0"));
    };
    o.valueOf = o.toString = function(){
        var o = this;
        return (o._s ? "-" : "") + (o._d.slice(0, o._f).join("") || "0") + (o._f != o._d.length ? "." + o._d.slice(o._f).join("") : "");
    };
    o._zeroes = function(n, l, t){
        var s = ["push", "unshift"][t || 0];
        for(++l; --l;  n[s](0));
        return n;
    };
    o.round = function(){
        if("_rounding" in this) return this;
        var $ = BigNumber, r = this.roundType, b = this._d, d, p, n, x;
        for(this._rounding = true; this._f > 1 && !b[0]; --this._f, b.shift());
        for(d = this._f, p = this.precision + d, n = b[p]; b.length > d && !b[b.length -1]; b.pop());
        x = (this._s ? "-" : "") + (p - d ? "0." + this._zeroes([], p - d - 1).join("") : "") + 1;
        if(b.length > p){
            n && (r == $.DOWN ? false : r == $.UP ? true : r == $.CEIL ? !this._s
            : r == $.FLOOR ? this._s : r == $.HALF_UP ? n >= 5 : r == $.HALF_DOWN ? n > 5
            : r == $.HALF_EVEN ? n >= 5 && b[p - 1] & 1 : false) && this.add(x);
            b.splice(p, b.length - p);
        }
        return delete this._rounding, this;
    };
}

var isNegZero = function(x) {return x === 0 && Math.atan2(x,x) < 0}

var _mod = {
    __getattr__: function(attr){
        $B.check_nb_args('__getattr__ ', 1, arguments)
        $B.check_no_kw('__getattr__ ', attr)

        var res = this[attr]
        if(res === undefined){$raise('AttributeError',
            'module math has no attribute ' + attr)}
        return res
    },
    acos: function(x){
        $B.check_nb_args('acos', 1, arguments)
        $B.check_no_kw('acos', x)
        return float.$factory(Math.acos(float_check(x)))
    },
    acosh: function(x){
        $B.check_nb_args('acosh', 1, arguments)
        $B.check_no_kw('acosh', x)

        if(_b_.$isinf(x)){return float.$factory('inf')}
        var y = float_check(x)
        return float.$factory(Math.log(y + Math.sqrt(y * y - 1)))
    },
    asin: function(x){
        $B.check_nb_args('asin', 1, arguments)
        $B.check_no_kw('asin', x)
        return float.$factory(Math.asin(float_check(x)))
    },
    asinh: function(x){
        $B.check_nb_args('asinh', 1, arguments)
        $B.check_no_kw('asinh', x)

        if(_b_.$isninf(x)){return float.$factory('-inf')}
        if(_b_.$isinf(x)){return float.$factory('inf')}
        var y = float_check(x)
        return float.$factory(Math.log(y + Math.sqrt(y * y + 1)))
    },
    atan: function(x){
        $B.check_nb_args('atan', 1, arguments)
        $B.check_no_kw('atan', x)

        if(_b_.$isninf(x)){return float.$factory(-Math.PI / 2)}
        if(_b_.$isinf(x)){return float.$factory(Math.PI / 2)}
        return float.$factory(Math.atan(float_check(x)))
    },
    atan2: function(y, x){
        $B.check_nb_args('atan2', 2, arguments)
        $B.check_no_kw('atan2', y, x)

        return float.$factory(Math.atan2(float_check(y), float_check(x)))
    },
    atanh: function(x){
        $B.check_nb_args('atanh', 1, arguments)
        $B.check_no_kw('atanh', x)

       var y = float_check(x)
       if(y == 0){return 0}
       return float.$factory(0.5 * Math.log((1 / y + 1)/(1 / y - 1)));
    },
    ceil: function(x){
        $B.check_nb_args('ceil', 1, arguments)
        $B.check_no_kw('ceil', x)

       try{return getattr(x, '__ceil__')()}catch(err){}

       if(_b_.$isninf(x)){return float.$factory('-inf')}
       if(_b_.$isinf(x)){return float.$factory('inf')}
       if(isNaN(x)){return float.$factory('nan')}

       var y = float_check(x)
       if(! isNaN(parseFloat(y)) && isFinite(y)){
           return int.$factory(Math.ceil(y))
       }

       $raise('ValueError',
           'object is not a number and does not contain __ceil__')
    },
    copysign: function(x, y){
        $B.check_nb_args('copysign', 2, arguments)
        $B.check_no_kw('copysign', x,y)

        var x1 = Math.abs(float_check(x))
        var y1 = float_check(y)
        var sign = Math.sign(y1)
        sign = (sign == 1 || Object.is(sign, +0)) ? 1 : - 1
        return float.$factory(x1 * sign)
    },
    cos : function(x){
        $B.check_nb_args('cos ', 1, arguments)
        $B.check_no_kw('cos ', x)
        return float.$factory(Math.cos(float_check(x)))
    },
    cosh: function(x){
        $B.check_nb_args('cosh', 1, arguments)
        $B.check_no_kw('cosh', x)

        if(_b_.$isinf(x)) {return float.$factory('inf')}
        var y = float_check(x)
        if(Math.cosh !== undefined){return float.$factory(Math.cosh(y))}
        return float.$factory((Math.pow(Math.E, y) +
            Math.pow(Math.E, -y)) / 2)
    },
    degrees: function(x){
        $B.check_nb_args('degrees', 1, arguments)
        $B.check_no_kw('degrees', x)
        return float.$factory(float_check(x) * 180 / Math.PI)
    },
    e: float.$factory(Math.E),
    erf: function(x){
        $B.check_nb_args('erf', 1, arguments)
        $B.check_no_kw('erf', x)

        // inspired from
        // http://stackoverflow.com/questions/457408/is-there-an-easily-available-implementation-of-erf-for-python
        var y = float_check(x)
        var t = 1.0 / (1.0 + 0.5 * Math.abs(y))
        var ans = 1 - t * Math.exp( -y * y - 1.26551223 +
                     t * ( 1.00002368 +
                     t * ( 0.37409196 +
                     t * ( 0.09678418 +
                     t * (-0.18628806 +
                     t * ( 0.27886807 +
                     t * (-1.13520398 +
                     t * ( 1.48851587 +
                     t * (-0.82215223 +
                     t * 0.17087277)))))))))
        if(y >= 0.0){return ans}
        return -ans
    },
    erfc: function(x){

        $B.check_nb_args('erfc', 1, arguments)
        $B.check_no_kw('erfc', x)

        // inspired from
        // http://stackoverflow.com/questions/457408/is-there-an-easily-available-implementation-of-erf-for-python
        var y = float_check(x)
        var t = 1.0 / (1.0 + 0.5 * Math.abs(y))
        var ans = 1 - t * Math.exp( -y * y - 1.26551223 +
                     t * ( 1.00002368 +
                     t * ( 0.37409196 +
                     t * ( 0.09678418 +
                     t * (-0.18628806 +
                     t * ( 0.27886807 +
                     t * (-1.13520398 +
                     t * ( 1.48851587 +
                     t * (-0.82215223 +
                     t * 0.17087277)))))))))
        if(y >= 0.0){return 1 - ans}
        return 1 + ans
    },
    exp: function(x){
        $B.check_nb_args('exp', 1, arguments)
        $B.check_no_kw('exp', x)

         if(_b_.$isninf(x)){return float.$factory(0)}
         if(_b_.$isinf(x)){return float.$factory('inf')}
         var _r = Math.exp(float_check(x))
         if(_b_.$isinf(_r)){throw OverflowError("math range error")}
         return float.$factory(_r)
    },
    expm1: function(x){
        $B.check_nb_args('expm1', 1, arguments)
        $B.check_no_kw('expm1', x)

         if(_b_.$isninf(x)){return float.$factory(0)}
         if(_b_.$isinf(x)){return float.$factory('inf')}
         var _r = Math.expm1(float_check(x))
         if(_b_.$isinf(_r)){throw OverflowError("math range error")}
         return float.$factory(_r)
    },
    //fabs: function(x){ return x>0?float.$factory(x):float.$factory(-x)},
    fabs: function(x){
        $B.check_nb_args('fabs', 1, arguments)
        $B.check_no_kw('fabs', x)
        return _b_.$fabs(x) // located in py_float.js
    },
    factorial: function(x){
        $B.check_nb_args('factorial', 1, arguments)
        $B.check_no_kw('factorial', x)

         //using code from http://stackoverflow.com/questions/3959211/fast-factorial-function-in-javascript
         var y = float_check(x),
             r = 1
         for(var i = 2; i <= y; i++){r *= i}
         return r
    },
    floor: function(x){
        $B.check_nb_args('floor', 1, arguments)
        $B.check_no_kw('floor', x)
        return Math.floor(float_check(x))
    },
    fmod: function(x,y){
        $B.check_nb_args('fmod', 2, arguments)
        $B.check_no_kw('fmod', x,y)
        return float.$factory(float_check(x) % float_check(y))
    },
    frexp: function(x){
        $B.check_nb_args('frexp', 1, arguments)
        $B.check_no_kw('frexp', x)

        var _l = _b_.$frexp(x)
        return _b_.tuple.$factory([float.$factory(_l[0]), _l[1]])
    },
    fsum: function(x){
        $B.check_nb_args('fsum', 1, arguments)
        $B.check_no_kw('fsum', x)

        /* Translation into Javascript of the function msum in an Active
           State Cookbook recipe : https://code.activestate.com/recipes/393090/
           by Raymond Hettinger
        */
        var partials = [],
            res = new Number(),
            _it = _b_.iter(x)
        while(true){
            try{
                var x = _b_.next(_it),
                    i = 0
                for(var j = 0, len = partials.length; j < len; j++){
                    var y = partials[j]
                    if(Math.abs(x) < Math.abs(y)){
                        var z = x
                        x = y
                        y = z
                    }
                    var hi = x + y,
                        lo = y - (hi - x)
                    if(lo){
                        partials[i] = lo
                        i++
                    }
                    x = hi
                }
                partials = partials.slice(0, i).concat([x])
            }catch(err){
                if(_b_.isinstance(err, _b_.StopIteration)){break}
                throw err
            }
        }
        var res = new Number(0)
        for(var i = 0; i < partials.length; i++){
            res += new Number(partials[i])
        }
        return new Number(res)
    },
    gamma: function(x){
        $B.check_nb_args('gamma', 1, arguments)
        $B.check_no_kw('gamma', x)

        if(_b_.isinstance(x, int)){
            if(i < 1){
                throw _b_.ValueError.$factory("math domain error")
            }
            var res = 1
            for(var i = 1; i < x; i++){res *= i}
            return new Number(res)
        }
        // Adapted from https://en.wikipedia.org/wiki/Lanczos_approximation
        var p = [676.5203681218851,
            -1259.1392167224028,
            771.32342877765313,
            -176.61502916214059,
            12.507343278686905,
            -0.13857109526572012,
            9.9843695780195716e-6,
            1.5056327351493116e-7
            ]

        var EPSILON = 1e-07
        function drop_imag(z){
            if(Math.abs(z.imag) <= EPSILON){
                z = z.real
            }
            return z
        }
        var z = x
        if(z < 0.5){
            var y = Math.PI / (Math.sin(Math.PI * z) * _mod.gamma(1-z)) // Reflection formula
        }else{
            z -= 1
            var x = 0.99999999999980993,
                i = 0
            for(var i = 0, len = p.length; i < len; i++){
                var pval = p[i]
                x += pval / (z + i + 1)
            }
            var t = z + p.length - 0.5,
                sq = Math.sqrt(2 * Math.PI),
                y = sq * Math.pow(t, (z + 0.5)) * Math.exp(-t) * x
        }
        return drop_imag(y)
    },
    gcd: function(){
        var $ = $B.args("gcd", 2, {a: null, b: null}, ['a', 'b'],
                arguments, {}, null, null),
            a = $B.PyNumber_Index($.a),
            b = $B.PyNumber_Index($.b)
        if(a == 0 && b == 0){return 0}
        // https://stackoverflow.com/questions/17445231/js-how-to-find-the-greatest-common-divisor
        a = Math.abs(a);
        b = Math.abs(b);
        if(b > a){var temp = a; a = b; b = temp;}
        while(true){
            if(b == 0){return a}
            a %= b
            if(a == 0){return b}
            b %= a
        }
    },
    hypot: function(x, y){
        $B.check_nb_args('hypot', 2, arguments)
        $B.check_no_kw('hypot', x,y)

       if(_b_.$isinf(x) || _b_.$isinf(y)){return float.$factory('inf')}
       var x1 = float_check(x),
           y1 = float_check(y)
       return float.$factory(Math.sqrt(x1 * x1 + y1 * y1))
    },
    inf: float.$factory('inf'),
    isclose: function(){
        var $ns = $B.args("isclose",
                          4,
                          {a: null, b: null, rel_tol: null, abs_tol: null},
                          ['a', 'b', 'rel_tol', 'abs_tol'],
                          arguments,
                          {rel_tol: 1e-09, abs_tol: 0.0},
                          null,
                          null)
        var a = $ns['a'],
            b = $ns['b'],
            rel_tol = $ns['rel_tol'],
            abs_tol = $ns['abs_tol']
        if(rel_tol < 0.0 || abs_tol < 0.0){
            throw ValueError('tolerances must be non-negative')
        }
        if(a == b){return True}
        if(_b_.$isinf(a) || _b_.$isinf(b)){return false}
        var diff = _b_.$fabs(b - a)
        var result = (
            (diff <= _b_.$fabs(rel_tol * b)) ||
                (diff <= _b_.$fabs(rel_tol * a))
            ) || (diff <= _b_.$fabs(abs_tol)
        )
        return result
    },
    isfinite: function(x){
        $B.check_nb_args('isfinite', 1, arguments)
        $B.check_no_kw('isfinite', x)
        return isFinite(float_check(x))
    },
    isinf: function(x){
        $B.check_nb_args('isinf', 1, arguments)
        $B.check_no_kw('isinf', x)
        return _b_.$isinf(float_check(x))
    },
    isnan: function(x){
        $B.check_nb_args('isnan', 1, arguments)
        $B.check_no_kw('isnan', x)
        return isNaN(float_check(x))
    },
    ldexp: function(x, i){
        $B.check_nb_args('ldexp', 2, arguments)
        $B.check_no_kw('ldexp', x, i)
        return _b_.$ldexp(x, i)   //located in py_float.js
    },
    lgamma: function(x){
        $B.check_nb_args('lgamma', 1, arguments)
        $B.check_no_kw('lgamma', x)

        return new Number(Math.log(Math.abs(_mod.gamma(x))))
    },
    log: function(x, base){
        var $ = $B.args("log", 2, {x: null, base: null}, ['x', 'base'],
            arguments, {base: _b_.None}, null, null),
            x = $.x,
            base = $.base

         var x1 = float_check(x)
         if(base === _b_.None){return float.$factory(Math.log(x1))}
         return float.$factory(Math.log(x1) / Math.log(float_check(base)))
    },
    log1p: function(x){
        $B.check_nb_args('log1p', 1, arguments)
        $B.check_no_kw('log1p', x)
        return float.$factory(Math.log1p(float_check(x)))
    },
    log2: function(x){
        $B.check_nb_args('log2', 1, arguments)
        $B.check_no_kw('log2', x)

        if(isNaN(x)){return float.$factory('nan')}
        if(_b_.$isninf(x)) {throw ValueError('')}
        var x1 = float_check(x)
        if(x1 < 0.0){throw ValueError('')}
        return float.$factory(Math.log(x1) / Math.LN2)
    },
    log10: function(x){
        $B.check_nb_args('log10', 1, arguments)
        $B.check_no_kw('log10', x)

        return float.$factory(Math.log10(float_check(x)))
    },
    modf: function(x){
        $B.check_nb_args('modf', 1, arguments)
        $B.check_no_kw('modf', x)

       if(_b_.$isninf(x)){
           return _b_.tuple.$factory([0.0, float.$factory('-inf')])
       }
       if(_b_.$isinf(x)){
           return _b_.tuple.$factory([0.0, float.$factory('inf')])
       }
       if(isNaN(x)){
           return _b_.tuple.$factory([float.$factory('nan'),
               float.$factory('nan')])
       }

       var x1 = float_check(x)
       if(x1 > 0){
          var i = float.$factory(x1 - Math.floor(x1))
          return _b_.tuple.$factory([i, float.$factory(x1 - i)])
       }

       var x2 = Math.ceil(x1)
       var i = float.$factory(x1 - x2)
       return _b_.tuple.$factory([i, float.$factory(x2)])
    },
    nan: float.$factory('nan'),
    pi : float.$factory(Math.PI),
    pow: function(x, y){
        $B.check_nb_args('pow', 2, arguments)
        $B.check_no_kw('pow', x,y)

        var x1 = float_check(x)
        var y1 = float_check(y)
        if(y1 == 0){return float.$factory(1)}
        if(x1 == 0 && y1 < 0){throw _b_.ValueError('')}

        if(isNaN(y1)){
            if(x1 == 1){return float.$factory(1)}
            return float.$factory('nan')
        }
        if(x1 == 0){return float.$factory(0)}

        if(_b_.$isninf(y)){
            if(x1 == 1 || x1 == -1){return float.$factory(1)}
            if(x1 < 1 && x1 > -1){return float.$factory('inf')}
            return float.$factory(0)
        }
        if(_b_.$isinf(y)){
            if(x1 == 1 || x1 == -1){return float.$factory(1)}
            if(x1 < 1 && x1 > -1){return float.$factory(0)}
            return float.$factory('inf')
        }

        if(isNaN(x1)){return float.$factory('nan')}
        if(_b_.$isninf(x)){
            if(y1 > 0 && isOdd(y1)){return float.$factory('-inf')}
            if(y1 > 0){return float.$factory('inf')}  // this is even or a float
            if(y1 < 0){return float.$factory(0)}
            return float.$factory(1)
        }

        if(_b_.$isinf(x)){
            if(y1 > 0){return float.$factory('inf')}
            if(y1 < 0){return float.$factory(0)}
            return float.$factory(1)
        }

        var r
        if(isLargeNumber(x1) || isLargeNumber(y1)){
           var x = new BigNumber(x1),
               y = new BigNumber(y1)
           r = x.pow(y)
        }else{
           r = Math.pow(x1,y1)
        }

        if(isNaN(r)){return float.$factory('nan')}
        if(_b_.$isninf(r)){return float.$factory('-inf')}
        if(_b_.$isinf(r)){return float.$factory('inf')}

        return r
    },
    radians: function(x){
        $B.check_nb_args('radians', 1, arguments)
        $B.check_no_kw('radians', x)

        return float.$factory(float_check(x) * Math.PI / 180)
    },
    sin : function(x){
        $B.check_nb_args('sin ', 1, arguments)
        $B.check_no_kw('sin ', x)
        return float.$factory(Math.sin(float_check(x)))},
    sinh: function(x) {
        $B.check_nb_args('sinh', 1, arguments)
        $B.check_no_kw('sinh', x)

        var y = float_check(x)
        if(Math.sinh !== undefined){return float.$factory(Math.sinh(y))}
        return float.$factory(
            (Math.pow(Math.E, y) - Math.pow(Math.E, -y)) / 2)
    },
    sqrt: function(x){
        $B.check_nb_args('sqrt ', 1, arguments)
        $B.check_no_kw('sqrt ', x)

      var y = float_check(x)
      if(y < 0){throw ValueError("math range error")}
      if(_b_.$isinf(y)){return float.$factory('inf')}
      var _r = Math.sqrt(y)
      if(_b_.$isinf(_r)){throw OverflowError("math range error")}
      return float.$factory(_r)
    },
    tan: function(x) {
        $B.check_nb_args('tan', 1, arguments)
        $B.check_no_kw('tan', x)

        var y = float_check(x)
        return float.$factory(Math.tan(y))
    },
    tanh: function(x) {
        $B.check_nb_args('tanh', 1, arguments)
        $B.check_no_kw('tanh', x)

        var y = float_check(x)
        if(Math.tanh !== undefined){return float.$factory(Math.tanh(y))}
        return float.$factory((Math.pow(Math.E, y) - Math.pow(Math.E, -y))/
             (Math.pow(Math.E, y) + Math.pow(Math.E, -y)))
    },
    trunc: function(x) {
        $B.check_nb_args('trunc', 1, arguments)
        $B.check_no_kw('trunc', x)

       try{return getattr(x, '__trunc__')()}catch(err){}
       var x1 = float_check(x)
       if(!isNaN(parseFloat(x1)) && isFinite(x1)){
          if(Math.trunc !== undefined){return int.$factory(Math.trunc(x1))}
          if(x1 > 0){return int.$factory(Math.floor(x1))}
          return int.$factory(Math.ceil(x1))  // x1 < 0
       }
       $raise('ValueError',
           'object is not a number and does not contain __trunc__')
    }
}

for(var $attr in _mod){
    if(typeof _mod[$attr] === 'function'){
        _mod[$attr].__repr__ = (function(func){
            return function(){return '<built-in function ' + func + '>'}
        })($attr)
        _mod[$attr].__str__ = (function(func){
            return function(){return '<built-in function ' + func + '>'}
        })($attr)
    }
}

return _mod

})(__BRYTHON__)
