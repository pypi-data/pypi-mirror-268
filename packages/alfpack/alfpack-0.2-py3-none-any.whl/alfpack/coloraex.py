from colorama import Fore, Back, Style

# Style normal
fnk = Style.NORMAL + Fore.BLACK            ; bnk = Style.NORMAL + Back.BLACK            ;
fnw = Style.NORMAL + Fore.WHITE            ; bnw = Style.NORMAL + Back.WHITE            ;

fnr = Style.NORMAL + Fore.RED              ; bnr = Style.NORMAL + Back.RED              ;
fny = Style.NORMAL + Fore.YELLOW           ; bny = Style.NORMAL + Back.YELLOW           ;
fng = Style.NORMAL + Fore.GREEN            ; bng = Style.NORMAL + Back.GREEN            ;
fnc = Style.NORMAL + Fore.CYAN             ; bnc = Style.NORMAL + Back.CYAN             ;
fnb = Style.NORMAL + Fore.BLUE             ; bnb = Style.NORMAL + Back.BLUE             ;
fnm = Style.NORMAL + Fore.MAGENTA          ; bnm = Style.NORMAL + Back.MAGENTA          ;

fnlr = Style.NORMAL + Fore.LIGHTRED_EX     ; bnlr = Style.NORMAL + Back.LIGHTRED_EX     ;
fnly = Style.NORMAL + Fore.LIGHTYELLOW_EX  ; bnly = Style.NORMAL + Back.LIGHTYELLOW_EX  ;
fnlg = Style.NORMAL + Fore.LIGHTGREEN_EX   ; bnlg = Style.NORMAL + Back.LIGHTGREEN_EX   ;
fnlc = Style.NORMAL + Fore.LIGHTCYAN_EX    ; bnlc = Style.NORMAL + Back.LIGHTCYAN_EX    ;
fnlb = Style.NORMAL + Fore.LIGHTBLUE_EX    ; bnlb = Style.NORMAL + Back.LIGHTBLUE_EX    ;
fnlm = Style.NORMAL + Fore.LIGHTMAGENTA_EX ; bnlm = Style.NORMAL + Back.LIGHTMAGENTA_EX ; 

# Style bright
fbk = Style.BRIGHT + Fore.BLACK            ; bbk = Style.BRIGHT + Back.BLACK            ;
fbw = Style.BRIGHT + Fore.WHITE            ; bbw = Style.BRIGHT + Back.WHITE            ;

fbr = Style.BRIGHT + Fore.RED              ; bbr = Style.BRIGHT + Back.RED              ;
fby = Style.BRIGHT + Fore.YELLOW           ; bby = Style.BRIGHT + Back.YELLOW           ;
fbg = Style.BRIGHT + Fore.GREEN            ; bbg = Style.BRIGHT + Back.GREEN            ;
fbc = Style.BRIGHT + Fore.CYAN             ; bbc = Style.BRIGHT + Back.CYAN             ;
fbb = Style.BRIGHT + Fore.BLUE             ; bbb = Style.BRIGHT + Back.BLUE             ;
fbm = Style.BRIGHT + Fore.MAGENTA          ; bbm = Style.BRIGHT + Back.MAGENTA          ;

fblr = Style.BRIGHT + Fore.LIGHTRED_EX     ; bblr = Style.BRIGHT + Back.LIGHTRED_EX     ;
fbly = Style.BRIGHT + Fore.LIGHTYELLOW_EX  ; bbly = Style.BRIGHT + Back.LIGHTYELLOW_EX  ;
fblg = Style.BRIGHT + Fore.LIGHTGREEN_EX   ; bblg = Style.BRIGHT + Back.LIGHTGREEN_EX   ;
fblc = Style.BRIGHT + Fore.LIGHTCYAN_EX    ; bblc = Style.BRIGHT + Back.LIGHTCYAN_EX    ;
fblb = Style.BRIGHT + Fore.LIGHTBLUE_EX    ; bblb = Style.BRIGHT + Back.LIGHTBLUE_EX    ;
fblm = Style.BRIGHT + Fore.LIGHTMAGENTA_EX ; bblm = Style.BRIGHT + Back.LIGHTMAGENTA_EX ; 

# Style dim
fdk = Style.DIM + Fore.BLACK            ; bdk = Style.DIM + Back.BLACK            ;
fdw = Style.DIM + Fore.WHITE            ; bdw = Style.DIM + Back.WHITE            ;

fdr = Style.DIM + Fore.RED              ; bdr = Style.DIM + Back.RED              ;
fdy = Style.DIM + Fore.YELLOW           ; bdy = Style.DIM + Back.YELLOW           ;
fdg = Style.DIM + Fore.GREEN            ; bdg = Style.DIM + Back.GREEN            ;
fdc = Style.DIM + Fore.CYAN             ; bdc = Style.DIM + Back.CYAN             ;
fdb = Style.DIM + Fore.BLUE             ; bdb = Style.DIM + Back.BLUE             ;
fdm = Style.DIM + Fore.MAGENTA          ; bdm = Style.DIM + Back.MAGENTA          ;

fdlr = Style.DIM + Fore.LIGHTRED_EX     ; bdlr = Style.DIM + Back.LIGHTRED_EX     ;
fdly = Style.DIM + Fore.LIGHTYELLOW_EX  ; bdly = Style.DIM + Back.LIGHTYELLOW_EX  ;
fdlg = Style.DIM + Fore.LIGHTGREEN_EX   ; bdlg = Style.DIM + Back.LIGHTGREEN_EX   ;
fdlc = Style.DIM + Fore.LIGHTCYAN_EX    ; bdlc = Style.DIM + Back.LIGHTCYAN_EX    ;
fdlb = Style.DIM + Fore.LIGHTBLUE_EX    ; bdlb = Style.DIM + Back.LIGHTBLUE_EX    ;
fdlm = Style.DIM + Fore.LIGHTMAGENTA_EX ; bdlm = Style.DIM + Back.LIGHTMAGENTA_EX ; 

# Style 
sb = Style.BRIGHT
sn = Style.NORMAL
sd = Style.DIM

# Reset
rf, rb = Fore.RESET, Back.RESET
ra = Style.RESET_ALL


forel = {'NORMAL' : [fnk, fnw, fnr, fny, fng, fnc, fnb, fnm, fnlr, fnly, fnlg, fnlc, fnlb, fnlm],
		 'BRIGHT' : [fbk, fbw, fbr, fby, fbg, fbc, fbb, fbm, fblr, fbly, fblg, fblc, fblb, fblm],
		 'DIM'    : [fdk, fdw, fdr, fdy, fdg, fdc, fdb, fdm, fdlr, fdly, fdlg, fdlc, fdlb, fdlm]}
backl = {'NORMAL' : [bnk, bnw, bnr, bny, bng, bnc, bnb, bnm, bnlr, bnly, bnlg, bnlc, bnlb, bnlm],
		 'BRIGHT' : [bbk, bbw, bbr, bby, bbg, bbc, bbb, bbm, bblr, bbly, bblg, bblc, bblb, bblm],
		 'DIM'    : [bdk, bdw, bdr, bdy, bdg, bdc, bdb, bdm, bdlr, bdly, bdlg, bdlc, bdlb, bdlm]}

namel = ['k', 'w', 'r', 'y', 'g', 'c', 'b', 'm', 'lr', 'ly', 'lg', 'lc', 'lb', 'lm']


def replace(s, char, color, test=False):

	print(s)
	print(s.replace(char, f"{color}{char}{ra}"))

	return s.replace(char, f"{color}{char}{ra}")

def testColor(full=False):

	if full:

		print(f"\nTest coloraex FULL")

		for name_style, style in zip(['BRIGHT', 'NORMAL', 'DIM'], ['b', 'n', 'd']):

			print(f"\nStyle {name_style:6} : ")

			for name_back, b in zip(namel, backl[name_style]):

				l = f" b{style}{name_back:2} : {b} "

				for name_fore, fore in zip(namel, forel[name_style]):

					l += f"{fore}f{style}{name_fore}{rf} "

				print(f"{l}{ra}")


	else:

		print(f"\nTest coloraex")

		for name_style, style in zip(['BRIGHT', 'NORMAL', 'DIM'], ['b', 'n', 'd']):

			l = f"Style {name_style:6} : "

			for name, fore in zip(namel, forel[name_style]):

				l += f"{fore}f{style}{name}{rf} "

			print(f"{l}{ra}")