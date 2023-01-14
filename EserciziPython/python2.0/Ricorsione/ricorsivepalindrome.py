def nodoubleRicor(str):
#@param str: string 
  newStr=""
  if len(str)==1:
    return newStr
  if str[0]!=str[1]:
    newStr+=str[1:]
    nodoubleRicor(str[1:])
  else:
    nodoubleRicor(str[1:])
  return newStr