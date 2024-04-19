import alfpack.coloraex as c
import json

col = [c.fng, c.fnlb, c.fbr, c.fby]
colType = {
	'dict' : c.fbk,
	'list' : c.fbk,
	'str' : None,
	'int' : c.fnlm,
	'float' : c.fnlm,
	'bool' : [c.bnr + c.fnk, c.bnlg + c.fnk],
	'none' : c.bny + c.fnk
}

class TooDeepDesc(Exception):

    def __init__(self, nbdeep):
        self.message = f"{c.fnr}Trop de level dans l'objet (over {nbdeep}){c.ra} -> il peut être augmenter avec l'argument `{c.fny}maxIteration{c.ra}` (si ce n'est pas fait exprès ...)"
        super().__init__(self.message)

def json2dict(jsonfilepath):

	with open(jsonfilepath, 'r', encoding='utf-8') as f:

		cont = f.read()
		return json.loads(cont)



def jsonType(jsonfilepath, **kwargs):

	data = json2dict("./test/test.json")
	dictType(data, **kwargs)


def listType(d, **kwargs):
	dictType(d, **kwargs)


def dictType(d, p=0, maxIteration=20, preffix="|", delimiter="    ", lenstr=96, save=[], hides=[], showPreffix=False,
				preffixReduction=True, preffixMaxLen=8, alignKeys=False, alignChar='.'):

	# On verifie que l'on est pas trop profond dans l'objet
	if p > maxIteration:
		raise TooDeepDesc(maxIteration)

	pp = ''

	if type(d) == dict:

		vals = d.values()

		if not showPreffix : pp = '* '

		if alignKeys:
			nbRemp = max([len(ki) for ki in d.keys()])
			trueKeys = [f"{key + alignChar*(nbRemp-len(key))}" for key in d.keys()]
		else : trueKeys = list(d.keys())
	
	else:

		if not showPreffix : pp = '| '
		vals = d
		trueKeys = list(range(len(d)))


	keys = [f"{col[p%len(col)]}{p:02}{c.fbk}{preffix}{c.ra}{pp}{col[p%len(col)]}{key}{c.ra} :" for key in trueKeys]
	pref = trueKeys

	for key, val, pre in zip(keys, vals, pref):

		isShow = True
		for hide in hides:
			if hide in key:
				isShow = False

		if isShow:

			if type(val) == dict or type(val) == list:


				if type(val) == dict : print(f"{key} {colType['dict']}dict [{len(val)}]{c.ra}")
				if type(val) == list : print(f"{key} {colType['list']}list [{len(val)}]{c.ra}")

				if showPreffix:
					if preffixReduction and len(str(pre)) >= preffixMaxLen : add_preffix = f"{str(pre)[:preffixMaxLen-1]}./"
					else : add_preffix = f"{pre}/"
				else:
					add_preffix = delimiter

				save = dictType(val, p=p+1, maxIteration=maxIteration, preffix=preffix+add_preffix, delimiter=delimiter, 
					lenstr=lenstr, save=save, hides=hides, showPreffix=showPreffix,
					preffixReduction=preffixReduction, preffixMaxLen=preffixMaxLen, 
					alignKeys=alignKeys, alignChar=alignChar)


			elif type(val) == str:
				if len(val) < lenstr:
					pval = f"`{val}`"
				else:
					pval = f"`{val[:lenstr]}...`"
				print(f"{key} {pval}")

			elif type(val) == int:
				print(f"{key} {colType['int']}{val}{c.ra}")

			elif type(val) == float:
				print(f"{key} {colType['float']}{val}{c.ra}")

			elif type(val) == bool:
				if val == False:
					print(f"{key} {colType['bool'][0]}False{c.ra}")
				else:
					print(f"{key} {colType['bool'][1]}True{c.ra}")

			elif val is None:
				print(f"{key} {colType['none']}None{c.ra}")

			else:
				if type(val) not in save:
					save.append(type(val))
				print(f"{key} {c.fdr}{type(val)}{c.ra}")

		else:
			if type(val) == dict:
				print(f"{key} {c.bnw + c.fnk}Hide dict [{len(val)}]{c.ra}")

			elif type(val) == list:
				print(f"{key} {c.bnw + c.fnk}Hide list [{len(val)}]{c.ra}")


	if p != 0:
		return save
	elif len(save) > 0:
		print(f"\nMissing Type(s) : {save}")