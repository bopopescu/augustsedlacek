var aip_version_check = "1.0.1";

userFieldTemplates = new Object();
var counter = 0;
//TP: jak je to v sablone
userFieldTemplates[counter++] = 
{
  description : "field 190",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Zahlavi - Kartotecni zaznam",
  subfields : [["a","VOLATILE: Osobni jmeno"],["1","VOLATILE: Prijmi / Prijmeni"],["w","VOLATILE: Typ jmena"],["3","VOLATILE: Predikat"],["4","VOLATILE: Domicil"],["y","VOLATILE: Datace - z kartoteky"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["v","VOLATILE: Pribuzenske vztahy"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
//  subfields : [["a","VOLATILE: Osobni jmeno"],["1","VOLATILE: Prijmi / Prijmeni"],["3","VOLATILE: Predikat"],["4","VOLATILE: Domicil"],["w","VOLATILE: Typ jmena"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["y","VOLATILE: Datace - z kartoteky"],["v","VOLATILE: Pribuzenske vztahy"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
  tag : "190"
};
userFieldTemplates[counter++] = 
{
  description : "field 400",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Variantni jmeno",
  subfields : [["a","VOLATILE: Osobni jmeno"],["1","VOLATILE: Prijmi / Prijmeni"],["w","VOLATILE: Typ jmena"],["3","VOLATILE: Predikat"],["4","VOLATILE: Domicil"],["y","VOLATILE: Datace - z kartoteky"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["v","VOLATILE: Pribuzenske vztahy"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
  tag : "400"
};
userFieldTemplates[counter++] = 
{
  description : "field 500",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Alternativni jmeno",
  subfields : [["a","VOLATILE: Osobni jmeno"],["1","VOLATILE: Prijmi / Prijmeni"],["w","VOLATILE: Typ jmena"],["3","VOLATILE: Predikat"],["4","VOLATILE: Domicil"],["y","VOLATILE: Datace - z kartoteky"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["v","VOLATILE: Pribuzenske vztahy"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
  tag : "500"
};
userFieldTemplates[counter++] = 
{
  description : "field 667",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Neverejna poznamka",
  subfields : [["a","VOLATILE: Neverejna poznamka"]],
  tag : "667"
};
userFieldTemplates[counter++] = 
{
  description : "field 670",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Citace",
  subfields : [["a","VOLATILE: Citace"],["b","VOLATILE: Nalezena informace"],["x","VOLATILE: Cislo strany (svazku)"],["y","VOLATILE: Citace - zkratka"],["z","VOLATILE: Interni revokace"],["5","VOLATILE: Typ zdrojoveho dokumentu"],["9","VOLATILE: Mira nejistoty"],["l","VOLATILE: Jazyk textu"]],
  tag : "670"
};
userFieldTemplates[counter++] = 
{
  description : "field 678",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Biografie",
  subfields : [["a","VOLATILE: Biografie"]],
  tag : "678"
};
userFieldTemplates[counter++] = 
{
  description : "field 680",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Poznamky",
  subfields : [["i","VOLATILE: Poznamka"]],
  tag : "680"
};
userFieldTemplates[counter++] = 
{
  description : "field 690",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Heraldicke udaje",
  subfields : [["g","VOLATILE: Typ grafickeho prvku"],["a","VOLATILE: Heraldicke udaje"]],
  tag : "690"
};
userFieldTemplates[counter++] = 
{
  description : "field 700",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Osobni jmeno - Propojeni",
  subfields : [["a","VOLATILE: Osobni jmeno"],["1","VOLATILE: Prijmi / Prijmeni"],["w","VOLATILE: Typ jmena"],["3","VOLATILE: Predikat"],["4","VOLATILE: Domicil"],["y","VOLATILE: Datace - z kartoteky"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["v","VOLATILE: Pribuzenske vztahy"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
  tag : "700"
};
userFieldTemplates[counter++] = 
{
  description : "field 711",
  ind1 : "2",
  ind2 : " ",
  isControlfield : false,
  name : "Udalost - propojeni",
  subfields : [["a","VOLATILE: Udalost"],["c","VOLATILE: Misto konani"],["y","VOLATILE: Datace - z kartoteky"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
  tag : "711"
};
userFieldTemplates[counter++] = 
{
  description : "field 751",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Mistni nazev - propojeni",
  subfields : [["a","VOLATILE: Mistni nazev"],["y","VOLATILE: Datace - z kartoteky"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
  tag : "751"
};
userFieldTemplates[counter++] = 
{
  description : "field 451",
  ind1 : " ",
  ind2 : " ",
  isControlfield : false,
  name : "Variantní místní název",
  subfields : [["a","VOLATILE: Mistni nazev"],["y","VOLATILE: Datace - z kartoteky"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
//  subfields : [["a","VOLATILE: Mistni nazev"],["d","VOLATILE: Datace - mimo kartoteku"],["x","VOLATILE: Zpresneni"],["y","VOLATILE: Datace - z kartoteky"],["l","VOLATILE: Jazyk textu"],["9","VOLATILE: Mira nejistoty"]],
  tag : "451"
};

var fieldName = '';
userFieldOptions = new Object();


//TP: jak je to v roletce
userFieldOptions = {
  fields : {
    '0' : {value : '', description : 'choose field'},
//    '040' : {value : '040', description : 'Autor záznamu'},
    '190' : {value : '190', description : 'Záhlaví - Kartotéční záznam'},
    '400' : {value : '400', description : 'Variantní jméno'},
    '500' : {value : '500', description : 'Alternativní jméno'},
    '667' : {value : '667', description : 'Neverejna poznamka'},
    '670' : {value : '670', description : 'Citace'},
    '675' : {value : '675', description : 'Negativní citace'},
    '678' : {value : '678', description : 'Biografie'},
    '680' : {value : '680', description : 'Poznámky'},
    '690' : {value : '690', description : 'Heraldické údaje'},
    '700' : {value : '700', description : 'Osobní jméno - propojeni'},
    '711' : {value : '711', description : 'Udalost - propojeni'},
    '751' : {value : '751', description : 'Mistni nazev - propojeni'},
    '451' : {value : '451', description : 'Variantni mistni nazev'},
//    '856' : {value : '856', description : 'Obrazek'},
    '956' : {value : '856', description : 'Obrazek_956'},
//    '906' : {value : '906', description : 'Interní údaje o zpracování'},
    '950' : {value : '950', description : 'Status'},
//    '970' : {value : '970', description : 'Identifikator KZ'},
//    '980' : {value : '980', description : 'Identifikator zasuvky'}
  },
  subfields : {
    '0' : {
      '0' : {value: 'a', description: 'first choose field'}
    },
    '040' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Autor puvodniho zaznamu'},
      b : {value: 'b', description: 'Jazyk katalogizace'},
      d : {value: 'd', description: 'Autor uprav v zaznamu'}
    },
    '190' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Osobni jmeno'},
      1 : {value: '1', description: 'Prijmi / Prijmeni'},
      b : {value: 'b', description: 'Rimske cislice'},
      3 : {value: '3', description: 'Predikat'},
      4 : {value: '4', description: 'Domicil'},
      w : {value: 'w', description: 'Typ jmena'},
      c : {value: 'c', description: 'Tituly'},
      d : {value: 'd', description: 'Datace - mimo kartoteku'},
      x : {value: 'x', description: 'Zpresneni'},
      y : {value: 'y', description: 'Datace - z kartoteky'},
      z : {value: 'z', description: 'Geograficke zpresneni'},
      v : {value: 'v', description: 'Pribuzenske vztahy'},
      l : {value: 'l', description: 'Jazyk textu'},
      9 : {value: '9', description: 'Mira nejistoty'}
    },
    '400' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Osobni jmeno'},
      1 : {value: '1', description: 'Prijmi / Prijmeni'},
      b : {value: 'b', description: 'Rimske cislice'},
      3 : {value: '3', description: 'Predikat'},
      4 : {value: '4', description: 'Domicil'},
      c : {value: 'c', description: 'Tituly'},
      d : {value: 'd', description: 'Datace - mimo kartoteku'},
      x : {value: 'x', description: 'Zpresneni'},
      y : {value: 'y', description: 'Datace - z kartoteky'},
      z : {value: 'z', description: 'Geograficke zpresneni'},
      v : {value: 'v', description: 'Pribuzenske vztahy'},
      l : {value: 'l', description: 'Jazyk textu'},
      w : {value: 'w', description: 'Typ jmena'},
      9 : {value: '9', description: 'Mira nejistoty'}
    },
    '451' : {
      0 : {value : '', description : 'choose subfield'},
      w : {value: 'w', description: 'Typ vztahu'},
      a : {value: 'a', description: 'Mistni nazev'},
      d : {value: 'd', description: 'Datace - mimo kartoteku'},
      c : {value: 'c', description: 'Misto konani'},
      x : {value: 'x', description: 'Zpresneni'},
      y : {value: 'y', description: 'Datace - z kartoteky'},
      z : {value: 'z', description: 'Geograficke zpresneni'},
      v : {value: 'v', description: 'Formalni zpresneni'},
      l : {value: 'l', description: 'Jazyk textu'},
      9 : {value: '9', description: 'Mira nejistoty'}
    },
    '500' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Osobni jmeno'},
      1 : {value: '1', description: 'Prijmi / Prijmeni'},
      b : {value: 'b', description: 'Rimske cislice'},
      3 : {value: '3', description: 'Predikat'},
      4 : {value: '4', description: 'Domicil'},
      c : {value: 'c', description: 'Tituly'},
      d : {value: 'd', description: 'Datace - mimo kartoteku'},
      x : {value: 'x', description: 'Zpresneni'},
      y : {value: 'y', description: 'Datace - z kartoteky'},
      z : {value: 'z', description: 'Geograficke zpresneni'},
      v : {value: 'v', description: 'Pribuzenske vztahy'},
      l : {value: 'l', description: 'Jazyk textu'},
      w : {value: 'w', description: 'Typ jmena'},
      9 : {value: '9', description: 'Mira nejistoty'}
    },
    '667' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Neverejna poznamka'}
    },
    '670' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Citace'},
      b : {value: 'b', description: 'Nalezena informace'},
      x : {value: 'x', description: 'Cislo strany (svazku)'},
      y : {value: 'y', description: 'Citace - zkratka'},
      z : {value: 'z', description: 'Interní revokace'},
      5 : {value: '5', description: 'Typ zdrojoveho dokumentu'},
      9 : {value: '9', description: 'Mira nejistoty'},
      l : {value: 'l', description: 'Jazyk textu'}
    },
    '675' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Negativni citace'}
    },
    '678' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Biografie'}
    },
    '680' : {
      0 : {value : '', description : 'choose subfield'},
      i : {value: 'i', description: 'Poznamka'}
    },
    '690' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Heraldicke udaje'},
      g : {value: 'g', description: 'Typ grafického prvku'}
    },
    '700' : {
      0 : {value : '', description : 'choose subfield'},
      w : {value: 'w', description: 'Typ jmena'},
      a : {value: 'a', description: 'Osobni jmeno'},
      1 : {value: '1', description: 'Prijmi / Prijmeni'},
      b : {value: 'b', description: 'Rimske cislice'},
      3 : {value: '3', description: 'Predikat'},
      4 : {value: '4', description: 'Domicil'},
      c : {value: 'c', description: 'Tituly'},
      d : {value: 'd', description: 'Datace - mimo kartoteku'},
      x : {value: 'x', description: 'Zpresneni'},
      y : {value: 'y', description: 'Datace - z kartoteky'},
      z : {value: 'z', description: 'Geograficke zpresneni'},
      v : {value: 'v', description: 'Pribuzenske vztahy'},
      l : {value: 'l', description: 'Jazyk textu'},
      9 : {value: '9', description: 'Mira nejistoty'}
    },
    '711' : {
      0 : {value : '', description : 'choose subfield'},
      w : {value: 'w', description: 'Typ vztahu'},
      a : {value: 'a', description: 'Udalost'},
      d : {value: 'd', description: 'Datace - mimo kartoteku'},
      c : {value: 'c', description: 'Misto konani'},
      x : {value: 'x', description: 'Zpresneni'},
      y : {value: 'y', description: 'Datace - z kartoteky'},
      z : {value: 'z', description: 'Geograficke zpresneni'},
      v : {value: 'v', description: 'Formalni zpresneni'},
      l : {value: 'l', description: 'Jazyk textu'},
      9 : {value: '9', description: 'Mira nejistoty'}
    },
    '751' : {
      0 : {value : '', description : 'choose subfield'},
      w : {value: 'w', description: 'Typ vztahu'},
      a : {value: 'a', description: 'Mistni nazev'},
      d : {value: 'd', description: 'Datace - mimo kartoteku'},
      c : {value: 'c', description: 'Misto konani'},
      x : {value: 'x', description: 'Zpresneni'},
      y : {value: 'y', description: 'Datace - z kartoteky'},
      z : {value: 'z', description: 'Geograficke zpresneni'},
      v : {value: 'v', description: 'Formalni zpresneni'},
      l : {value: 'l', description: 'Jazyk textu'},
      9 : {value: '9', description: 'Mira nejistoty'}
    },
    '856' : {
      0 : {value : '', description : 'choose subfield'},
      u : {value: 'u', description: 'URL'},
      1 : {value: '1', description: 'Format listku'},
      9 : {value: '9', description: 'Zpusob natoceni'},
      y : {value: 'y', description: 'Nazev obrazku'}
    },
    '906' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Způsob zpracování + datace'},
      b : {value: 'b', description: 'Podpis katalogizátora'},
      c : {value: 'c', description: 'Druh opravy, doplnění'}
    },
    '950' : {
      0 : {value : '', description : 'choose subfield'},
      s : {value: 's', description: 'Status'},
      p : {value: 'p', description: 'Pokracujici listky'}
    },
    '956' : {
      0 : {value : '', description : 'choose subfield'},
      u : {value: 'u', description: 'URL'},
      1 : {value: '1', description: 'Format listku'},
      9 : {value: '9', description: 'Zpusob natoceni'},
      y : {value: 'y', description: 'Nazev obrazku'}
    },
    '970' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Identifikator KZ'}
    },
    '980' : {
      0 : {value : '', description : 'choose subfield'},
      a : {value: 'a', description: 'Identifikator zasuvky'}
    }
  }
};

function getSubfieldValues(code) {
  var values = undefined;
  switch (code) {
    case '190w':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'akronym', description : 'akronym'},
        '2' : {value : 'skutečné jméno', description : 'skutečné jméno'},
        '3' : {value : 'církevní jméno', description : 'církevní jméno'},
        '4' : {value : 'jméno získané sňatkem', description : 'jméno získané sňatkem'},
        '5' : {value : 'jméno za svobodna', description : 'jméno za svobodna'},
        '6' : {value : 'pseudonym', description : 'pseudonym'},
        '7' : {value : 'společný pseudonym', description : 'společný pseudonym'},
        '8' : {value : 'světské jméno', description : 'světské jméno'}
      }
      break;
    case '1009':
    case '1119':
    case '1519':
    case '1909':
    case '4009':
    case '4119':
    case '4519':
    case '5009':
    case '5119':
    case '5519':
    case '6709':
    case '7009':
    case '7119':
    case '7519':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'nejisté', description : 'nejisté'}
      }
      break;
    case '100c':
    case '190c':
    case '400c':
    case '500c':
    case '700c':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'arcivévoda/arcivévodkyně', description : 'arcivévoda/arcivévodkyně'},
        '2' : {value : 'císař/císařovna', description : 'císař/císařovna'},
        '3' : {value : 'hrabě/hraběnka', description : 'hrabě/hraběnka'},
        '4' : {value : 'kníže/kněžna', description : 'kníže/kněžna'},
        '5' : {value : 'král/královna', description : 'král/královna'},
        '6' : {value : 'landkrabě/landkraběnka', description : 'landkrabě/landkraběnka'},
        '7' : {value : 'man/leník', description : 'man/leník'},
        '8' : {value : 'markrabě/markraběnka', description : 'markrabě/markraběnka'},
        '9' : {value : 'měšťan/měšťanka', description : 'měšťan/měšťanka'},
        '10' : {value : 'pán/paní', description : 'pán/paní'},
        '11' : {value : 'rytíř/vladyka', description : 'rytíř/vladyka'},
        '12' : {value : 'vévoda/vévodkyně', description : 'vévoda/vévodkyně'}
      }
      break;
    case '400w':
    case '500w':
    case '700w':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'akronym', description : 'akronym'},
        '2' : {value : 'skutečné jméno', description : 'skutečné jméno'},
        '3' : {value : 'církevní jméno', description : 'církevní jméno'},
        '4' : {value : 'jméno získané sňatkem', description : 'jméno získané sňatkem'},
        '5' : {value : 'jméno za svobodna', description : 'jméno za svobodna'},
        '6' : {value : 'pseudonym', description : 'pseudonym'},
        '7' : {value : 'společný pseudonym', description : 'společný pseudonym'},
        '8' : {value : 'světské jméno', description : 'světské jméno'}
      }
      break;
    case '411w':
    case '511w':
    case '711w':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'dřívější záhlaví', description : 'dřívější záhlaví'},
        '2' : {value : 'novější záhlaví', description : 'novější záhlaví'},
        '3' : {value : 'bezprostředně vyšší nadřízený termín', description : 'bezprostředně vyšší nadřízený termín'}
      }
      break;
    case '551w':
    case '451w':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'dřívější záhlaví', description : 'dřívější záhlaví'},
        '2' : {value : 'novější záhlaví', description : 'novější záhlaví'},
        '3' : {value : 'širší termín', description : 'širší termín'},
        '4' : {value : 'užší termín', description : 'užší termín'},
        '5' : {value : 'bezprostředně vyšší nadřízený termín', description : 'bezprostředně vyšší nadřízený termín'}
      }
      break;
    case '751w':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'dřívější záhlaví', description : 'dřívější záhlaví'},
        '2' : {value : 'novější záhlaví', description : 'novější záhlaví'},
        '3' : {value : 'širší termín', description : 'širší termín'},
        '4' : {value : 'užší termín', description : 'užší termín'},
        '5' : {value : 'bezprostředně vyšší nadřízený termín', description : 'bezprostředně vyšší nadřízený termín'}
      }
    case '670a':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'Odkaz', description : 'Odkaz'},
        '2' : {value : 'Prázdný lístek', description : 'Prázdný lístek'},
        '3' : {value : 'Bez citace', description : 'Bez citace'}
      }
      break;
    case '670z':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'A', description : 'A'},
        '2' : {value : 'Arch.', description : 'Arch.'},
        '3' : {value : 'B', description : 'B'},
        '4' : {value : 'Bech.', description : 'Bech.'},
        '5' : {value : 'Bil.', description : 'Bil.'},
        '6' : {value : 'Bol. A', description : 'Bol. A'},
        '7' : {value : 'Bol. B', description : 'Bol. B'},
        '8' : {value : 'BU', description : 'BU'},
        '9' : {value : 'C', description : 'C'},
        '10' : {value : 'Coll. I.', description : 'Coll. I.'},
        '11' : {value : 'Coll. II.', description : 'Coll. II.'},
        '12' : {value : 'Cop. Przem.', description : 'Cop. Przem.'},
        '13' : {value : 'CT', description : 'CT'},
        '14' : {value : 'D', description : 'D'},
        '15' : {value : 'Dr (1-383/399)', description : 'Dr (1-383/399)'},
        '16' : {value : 'Dr (400 a výše) ', description : 'Dr (400 a výše) '},
        '17' : {value : 'DZ (1-361)', description : 'DZ (1-361)'},
        '18' : {value : 'DZ (362-910)', description : 'DZ (362-910)'},
        '19' : {value : 'DZ (911-1260)', description : 'DZ (911-1260)'},
        '20' : {value : 'DZ', description : 'DZ'},
        '21' : {value : 'E', description : 'E'},
        '22' : {value : 'Er (130-255)', description : 'Er (130-255)'},
        '23' : {value : 'Er (256-461)', description : 'Er (256-461)'},
        '24' : {value : 'F', description : 'F'},
        '25' : {value : 'Gen.', description : 'Gen.'},
        '26' : {value : 'Gr.  A', description : 'Gr.  A'},
        '27' : {value : 'Gr.  B', description : 'Gr.  B'},
        '28' : {value : 'Gub. I.', description : 'Gub. I.'},
        '29' : {value : 'Gub. II.', description : 'Gub. II.'},
        '30' : {value : 'Gub. III.', description : 'Gub. III.'},
        '31' : {value : 'Hors.', description : 'Hors.'},
        '32' : {value : 'Hrd.', description : 'Hrd.'},
        '33' : {value : 'Ch.', description : 'Ch.'},
        '34' : {value : 'Itin.', description : 'Itin.'},
        '35' : {value : 'K (1-439/499)', description : 'K (1-439/499)'},
        '36' : {value : 'K (500-615)', description : 'K (500-615)'},
        '37' : {value : 'Karlstein', description : 'Karlstein'},
        '38' : {value : 'Kr', description : 'Kr'},
        '39' : {value : 'Kniha opisů', description : 'Kniha opisů'},
        '40' : {value : 'Kur.', description : 'Kur.'},
        '41' : {value : 'L', description : 'L'},
        '42' : {value : 'Lit.', description : 'Lit.'},
        '43' : {value : 'Lt.', description : 'Lt.'},
        '44' : {value : 'Mal.', description : 'Mal.'},
        '45' : {value : 'Mikšovic', description : 'Mikšovic'},
        '46' : {value : 'Mor. I. (1-252) 125', description : 'Mor. I. (1-252) 125'},
        '47' : {value : 'Mor. I. (1-255) 126', description : 'Mor. I. (1-255) 126'},
        '48' : {value : 'Mor. I. (1-55) 127', description : 'Mor. I. (1-55) 127'},
        '49' : {value : 'Mn. I.', description : 'Mn. I.'},
        '50' : {value : 'Mn. II.', description : 'Mn. II.'},
        '51' : {value : 'Mix.', description : 'Mix.'},
        '52' : {value : 'Mus. (1-311)', description : 'Mus. (1-311)'},
        '53' : {value : 'Mus. II. (312-339)', description : 'Mus. II. (312-339)'},
        '54' : {value : 'N', description : 'N'},
        '55' : {value : 'Orl.', description : 'Orl.'},
        '56' : {value : 'Plz.', description : 'Plz.'},
        '57' : {value : 'Popis', description : 'Popis'},
        '58' : {value : 'Prag.', description : 'Prag.'},
        '59' : {value : 'Q', description : 'Q'},
        '60' : {value : 'Rud. A', description : 'Rud. A'},
        '61' : {value : 'Rud. B', description : 'Rud. B'},
        '62' : {value : 'SB', description : 'SB'},
        '63' : {value : 'Sil.', description : 'Sil.'},
        '64' : {value : 'T', description : 'T'},
        '65' : {value : 'Tepl.', description : 'Tepl.'},
        '66' : {value : 'Tr (1-22)', description : 'Tr (1-22)'},
        '67' : {value : 'Tr (22b-662i)', description : 'Tr (22b-662i)'},
        '68' : {value : 'Tr (663-1107)', description : 'Tr (663-1107)'},
        '69' : {value : 'Tr (1108-1450)', description : 'Tr (1108-1450)'},
        '70' : {value : 'Tr II.', description : 'Tr II.'},
        '71' : {value : 'Tr III.', description : 'Tr III.'},
        '72' : {value : 'Tr IV.', description : 'Tr IV.'},
        '73' : {value : 'Tyt.', description : 'Tyt.'},
        '74' : {value : 'Vat.', description : 'Vat.'},
        '75' : {value : 'V. II.', description : 'V. II.'},
        '76' : {value : 'Var.', description : 'Var.'},
        '77' : {value : 'V', description : 'V'},
        '78' : {value : 'Vind. I. (1-500)', description : 'Vind. I. (1-500)'},
        '79' : {value : 'Vind. II. (501 a výše)', description : 'Vind. II. (501 a výše)'},
        '80' : {value : 'Vind. III.', description : 'Vind. III.'},
        '81' : {value : 'Vind. IV.', description : 'Vind. IV.'},
        '82' : {value : 'Vis.', description : 'Vis.'},
        '83' : {value : 'W', description : 'W'},
        '84' : {value : 'Zacz.', description : 'Zacz.'},
        '85' : {value : 'Zap.', description : 'Zap.'}
      }
      break;
    case '670y':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'Arch. č. ', description : 'Arch. č. '},
        '2' : {value : 'Balbini Vita Arnesti ', description : 'Balbini Vita Arnesti '},
        '3' : {value : 'Balbini Tabular. ', description : 'Balbini Tabular. '},
        '4' : {value : 'B. Balbini Examen Melisseum ', description : 'B. Balbini Examen Melisseum '},
        '5' : {value : 'Balbín Misc. ', description : 'Balbín Misc. '},
        '6' : {value : 'Beck. ', description : 'Beck. '},
        '7' : {value : 'Berna Plz.', description : 'Berna Plz.'},
        '8' : {value : 'Bienenberg Gesch. Königgrätz ', description : 'Bienenberg Gesch. Königgrätz '},
        '8' : {value : 'Bílek konf. ', description : 'Bílek konf. '},
        '9' : {value : 'Borový Er. ', description : 'Borový Er. '},
        '10' : {value : 'Brandl Kn. Tovač. ', description : 'Brandl Kn. Tovač. '},
        '11' : {value : 'CDB ', description : 'CDB '},
        '12' : {value : 'CDL ', description : 'CDL '},
        '13' : {value : 'CDM ', description : 'CDM '},
        '14' : {value : 'ČČM ', description : 'ČČM '},
        '15' : {value : 'ČČM ', description : 'ČČM '},
        '16' : {value : 'ČČM ', description : 'ČČM '},
        '17' : {value : 'Č. Sp. P. ', description : 'Č. Sp. P. '},
        '18' : {value : 'DB', description : 'DB'},
        '19' : {value : 'DD', description : 'DD'},
        '20' : {value : 'DO', description : 'DO'},
        '21' : {value : 'DZ', description : 'DZ'},
        '22' : {value : 'Dačický ', description : 'Dačický '},
        '23' : {value : 'Demuth G. d. L. ', description : 'Demuth G. d. L. '},
        '24' : {value : 'Dobner Mon. ', description : 'Dobner Mon. '},
        '25' : {value : 'Dörr der Adel ', description : 'Dörr der Adel '},
        '26' : {value : 'Dvorský Paměti žen ', description : 'Dvorský Paměti žen '},
        '27' : {value : 'Emler Tab. vet. ', description : 'Emler Tab. vet. '},
        '28' : {value : 'Emler urbáře ', description : 'Emler urbáře '},
        '29' : {value : 'Font. r. Boh. ', description : 'Font. r. Boh. '},
        '30' : {value : 'Glafey Anecd. ', description : 'Glafey Anecd. '},
        '31' : {value : 'Glatzer Gesch. ', description : 'Glatzer Gesch. '},
        '32' : {value : 'Goll Čechy a Prusy ', description : 'Goll Čechy a Prusy '},
        '33' : {value : 'Heber´s Burgen ', description : 'Heber´s Burgen '},
        '34' : {value : 'Höfler ', description : 'Höfler '},
        '35' : {value : 'Chlumecký Reg. ', description : 'Chlumecký Reg. '},
        '36' : {value : 'Jirečk. Ruk. ', description : 'Jirečk. Ruk. '},
        '37' : {value : 'Jungm. h. l. ', description : 'Jungm. h. l. '},
        '38' : {value : 'Kapras Kn. sv. Bydžov. ', description : 'Kapras Kn. sv. Bydžov. '},
        '39' : {value : 'Kopecký Reg. ', description : 'Kopecký Reg. '},
        '40' : {value : 'Lupáč ', description : 'Lupáč '},
        '41' : {value : 'Mars Morav. ', description : 'Mars Morav. '},
        '42' : {value : 'Menčík Pam. Harant. ', description : 'Menčík Pam. Harant. '},
        '43' : {value : 'Miscellanea', description : 'Miscellanea'},
        '44' : {value : 'Mon. univ. Prag. ', description : 'Mon. univ. Prag. '},
        '45' : {value : 'Mon. Vat. ', description : 'Mon. Vat. '},
        '46' : {value : 'MVGDB ', description : 'MVGDB '},
        '47' : {value : 'Nedopil ', description : 'Nedopil '},
        '48' : {value : 'Neues Laus. Mag. ', description : 'Neues Laus. Mag. '},
        '49' : {value : 'Palacký ', description : 'Palacký '},
        '50' : {value : 'Palacký Doc. ', description : 'Palacký Doc. '},
        '51' : {value : 'Palacký formelb. ', description : 'Palacký formelb. '},
        '52' : {value : 'Palacký UB ', description : 'Palacký UB '},
        '53' : {value : 'Pam. arch. ', description : 'Pam. arch. '},
        '54' : {value : 'Pam. Dačického ', description : 'Pam. Dačického '},
        '55' : {value : 'Pangerl Die Witigonen ', description : 'Pangerl Die Witigonen '},
        '56' : {value : 'Pangerl G. U. ', description : 'Pangerl G. U. '},
        '57' : {value : 'Pangerl Hoh. Urk. ', description : 'Pangerl Hoh. Urk. '},
        '58' : {value : 'Paproc. o st. pan. ', description : 'Paproc. o st. pan. '},
        '59' : {value : 'Paproc. o st. ryt. ', description : 'Paproc. o st. ryt. '},
        '60' : {value : 'Pelzel Urkdbch ', description : 'Pelzel Urkdbch '},
        '61' : {value : 'Pescheck Exulanten ', description : 'Pescheck Exulanten '},
        '62' : {value : 'Podlaha Lib. conf. ', description : 'Podlaha Lib. conf. '},
        '63' : {value : 'Podlaha Lib. erect. ', description : 'Podlaha Lib. erect. '},
        '64' : {value : 'Podlaha Lib. ord. ', description : 'Podlaha Lib. ord. '},
        '65' : {value : 'Reg. ', description : 'Reg. '},
        '66' : {value : 'Rel. tab. ', description : 'Rel. tab. '},
        '67' : {value : 'RI', description : 'RI'},
        '68' : {value : 'Riegger Arch. ', description : 'Riegger Arch. '},
        '69' : {value : 'Rozvržení ', description : 'Rozvržení '},
        '70' : {value : 'Script. rer. Lus. ', description : 'Script. rer. Lus. '},
        '71' : {value : 'Schaller ', description : 'Schaller '},
        '72' : {value : 'Schaller Prag ', description : 'Schaller Prag '},
        '73' : {value : 'Schönfeld Adels Schematismus ', description : 'Schönfeld Adels Schematismus '},
        '74' : {value : 'Schriften ', description : 'Schriften '},
        '75' : {value : 'Schulz Soupis reg. soudu nejv. purkr. ', description : 'Schulz Soupis reg. soudu nejv. purkr. '},
        '76' : {value : 'Slavík Děje Vlašimě ', description : 'Slavík Děje Vlašimě '},
        '77' : {value : 'Sommer', description : 'Sommer'},
        '78' : {value : 'Soupis ', description : 'Soupis '},
        '79' : {value : 'St. letop. ', description : 'St. letop. '},
        '80' : {value : 'Steinbach ', description : 'Steinbach '},
        '81' : {value : 'Stocklöw Tachau ', description : 'Stocklöw Tachau '},
        '82' : {value : 'Strnad Listář Plzenský ', description : 'Strnad Listář Plzenský '},
        '83' : {value : 'Světecký', description : 'Světecký'},
        '84' : {value : 'Švenda Želez. obraz ', description : 'Švenda Želez. obraz '},
        '85' : {value : 'Tadra Acta iud. ', description : 'Tadra Acta iud. '},
        '86' : {value : 'Tadra Canc. Arn. ', description : 'Tadra Canc. Arn. '},
        '87' : {value : 'Tadra Kanceláře a písaři ', description : 'Tadra Kanceláře a písaři '},
        '88' : {value : 'Tadra Listy Zbrasl. ', description : 'Tadra Listy Zbrasl. '},
        '89' : {value : 'Teige Zákl. ', description : 'Teige Zákl. '},
        '90' : {value : 'Theobald ', description : 'Theobald '},
        '91' : {value : 'Tischer Dopisy ', description : 'Tischer Dopisy '},
        '92' : {value : 'Tomek Děje Prahy ', description : 'Tomek Děje Prahy '},
        '93' : {value : 'Truhlář Rukopisy ', description : 'Truhlář Rukopisy '},
        '94' : {value : 'Truhlář Rukověť ', description : 'Truhlář Rukověť '},
        '95' : {value : 'Vavákovy Pam. ', description : 'Vavákovy Pam. '},
        '96' : {value : 'Vávra Děj. Kolína ', description : 'Vávra Děj. Kolína '},
        '97' : {value : 'VČA ', description : 'VČA '},
        '98' : {value : 'Veleslav. Kal. ', description : 'Veleslav. Kal. '},
        '99' : {value : 'Wolný ', description : 'Wolný '},
        '100' : {value : 'ZDVM ', description : 'ZDVM '},
        '101' : {value : 'Zíbrt BČH ', description : 'Zíbrt BČH '},
        '102' : {value : 'Zíbrt z dějin Zvíkova ', description : 'Zíbrt z dějin Zvíkova '},
        '103' : {value : 'Zrc. ', description : 'Zrc. '}
      }
      break;
    case '6705':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'deskový vklad', description : 'deskový vklad'},
        '2' : {value : 'kronika', description : 'kronika'},
        '3' : {value : 'kupní listina', description : 'kupní listina'},
        '4' : {value : 'listina, list', description : 'listina, list'},
        '5' : {value : 'literární dílo', description : 'literární dílo (např. oslavné)'},
        '6' : {value : 'matrika', description : 'matrika'},
        '7' : {value : 'městská kniha', description : 'městská kniha'},
        '8' : {value : 'náhrobník/zmínka o pohřbu', description : 'náhrobník/zmínka o pohřbu'},
        '9' : {value : 'nápis', description : 'nápis (např. náhrobník, memoriální desk)'},
        '10' : {value : 'nekrologium/anniversarium', description : 'nekrologium/anniversarium'},
        '11' : {value : 'novinový výstřižek', description : 'novinový výstřižek'}
      }
      break;
    case '690g':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'erb/pečeť (popis a náčrt)', description : 'erb/pečeť (popis a náčrt)'},
        '2' : {value : 'erb/pečeť (popis)', description : 'erb/pečeť (popis)'},
        '3' : {value : 'erb/pečeť (náčrt)', description : 'erb/pečeť (náčrt)'},
        '4' : {value : 'erb/pečeť (zmínka)', description : 'erb/pečeť (zmínka)'},
        '5' : {value : 'genealogie', description : 'genealogie'},
        '6' : {value : 'plánek, situační nákres', description : 'plánek, situační nákres'},
        '7' : {value : 'pohlednice', description : 'pohlednice'}
      }
      break;
    case '711a':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'dědictví / dělení pozůstalosti', description : 'dědictví / dělení pozůstalosti'},
        '2' : {value : 'dluh/půjčka', description : 'dluh/půjčka'},
        '3' : {value : 'donace/nadace', description : 'donace/nadace'},
        '4' : {value : 'inkolát', description : 'inkolát'},
        '5' : {value : 'konfirmace', description : 'konfirmace'},
        '6' : {value : 'křest', description : 'křest'},
        '7' : {value : 'narození', description : 'narození'},
        '8' : {value : 'nobilitace', description : 'nobilitace'},
        '9' : {value : 'odúmrť', description : 'odúmrť'},
        '10' : {value : 'opověď', description : 'opověď'},
        '11' : {value : 'patronát / patronátní právo', description : 'patronát / patronátní právo'},
        '12' : {value : 'pohřeb', description : 'pohřeb'},
        '13' : {value : 'poručenství', description : 'poručenství'},
        '14' : {value : 'privilegium', description : 'privilegium'},
        '15' : {value : 'prodej/koupě', description : 'prodej/koupě'},
        '16' : {value : 'příměří', description : 'příměří'},
        '17' : {value : 'půhon/soudní pře/nález', description : 'půhon/soudní pře/nález'},
        '18' : {value : 'rukojmí / rukojemství', description : 'rukojmí / rukojemství'},
        '19' : {value : 'smlouva', description : 'smlouva'},
        '20' : {value : 'sňatek', description : 'sňatek'},
        '21' : {value : 'sněm/sjezd', description : 'sněm/sjezd'},
        '22' : {value : 'svatební smlouva', description : 'svatební smlouva'},
        '23' : {value : 'svědek', description : 'svědek'},
        '24' : {value : 'testament', description : 'testament'},
        '25' : {value : 'úmrtí', description : 'úmrtí'},
        '26' : {value : 'věnná zástava', description : 'věnná zástava'},
        '27' : {value : 'zástava', description : 'zástava'},
        '28' : {value : 'zmínka (prostá)', description : 'zmínka (prostá)'},
        '29' : {value : 'jiné', description : 'jiné'}
      }
      break;
    case '8561':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'běžná velikost lístku, 1 strana', description : 'běžná velikost lístku, 1 strana'},
        '2' : {value : 'běžná velikost lístku, 2 strany', description : 'běžná velikost lístku, 2 strany'},
        '3' : {value : 'běžná velikost lístku, text článku přilepen na 2. stranu', description : 'běžná velikost lístku, text článku přilepen na 2. stranu'},
        '4' : {value : 'větší než obvyklá velikost lístku', description : 'větší než obvyklá velikost lístku'},
        '5' : {value : 'menší než obvyklá velikost lístku', description : 'menší než obvyklá velikost lístku'}
      }
      break;
     case '8569':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : '0', description : '0'},
        '2' : {value : '90', description : '90'},
        '3' : {value : '180', description : '180'},
        '4' : {value : '270', description : '270'}
      }
      break;
     case '950s':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'nepřepsané', description : 'nepřepsané'},
        '2' : {value : 'přepsané', description : 'přepsané'},
        '3' : {value : 'na kontrolu', description : 'na kontrolu'}
      }
      break;
     case '950p':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'připojený k předchozímu', description : 'připojený k předchozímu'},
        '2' : {value : 'pokračující lístek', description : 'pokračující lístek'},
        '3' : {value : 'samostatný lístek', description : 'samostatný lístek'}
      }
      break;
    case '9561':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'běžná velikost lístku, 1 strana', description : 'běžná velikost lístku, 1 strana'},
        '2' : {value : 'běžná velikost lístku, 2 strany', description : 'běžná velikost lístku, 2 strany'},
        '3' : {value : 'běžná velikost lístku, text článku přilepen na 2. stranu', description : 'běžná velikost lístku, text článku přilepen na 2. stranu'},
        '4' : {value : 'větší než obvyklá velikost lístku', description : 'větší než obvyklá velikost lístku'},
        '5' : {value : 'menší než obvyklá velikost lístku', description : 'menší než obvyklá velikost lístku'}
      }
      break;
     case '9569':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : '0', description : '0'},
        '2' : {value : '90', description : '90'},
        '3' : {value : '180', description : '180'},
        '4' : {value : '270', description : '270'}
      }
      break;
     case '190x':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'nedat.', description : 'nedat.'},
        '2' : {value : 'nejst.', description : 'nejst.'},
        '3' : {value : 'st.', description : 'st.'},
        '4' : {value : 'ml.', description : 'ml.'},
        '5' : {value : 'nejml.', description : 'nejml.'}
      }
     case '400x':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'nedat.', description : 'nedat.'},
        '2' : {value : 'nejst.', description : 'nejst.'},
        '3' : {value : 'st.', description : 'st.'},
        '4' : {value : 'ml.', description : 'ml.'},
        '5' : {value : 'nejml.', description : 'nejml.'}
      }
     case '500x':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'nedat.', description : 'nedat.'},
        '2' : {value : 'nejst.', description : 'nejst.'},
        '3' : {value : 'st.', description : 'st.'},
        '4' : {value : 'ml.', description : 'ml.'},
        '5' : {value : 'nejml.', description : 'nejml.'}
      }
     case '700x':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'nedat.', description : 'nedat.'},
        '2' : {value : 'nejst.', description : 'nejst.'},
        '3' : {value : 'st.', description : 'st.'},
        '4' : {value : 'ml.', description : 'ml.'},
        '5' : {value : 'nejml.', description : 'nejml.'}
      }
      break;
     case '190l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '400l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '500l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '670l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '675l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '700l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '711l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '751l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '451l':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'čeština', description : 'čeština'},
        '2' : {value : 'latina', description : 'latina'},
        '3' : {value : 'němčina', description : 'němčina'},
        '4' : {value : 'francouzština', description : 'francouzština'},
        '5' : {value : 'jiný', description : 'jiný'}
      }
      break;
     case '190a':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'N.', description : 'N.'},
        '2' : {value : 'Prázdný lístek', description : 'Prázdný lístek'}
      }
      break;
     case '400a':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'N.', description : 'N.'}
      }
      break;
     case '500a':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'N.', description : 'N.'}
      }
      break;
     case '700a':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'N.', description : 'N.'}
      }
      break;
     case '190v':
     case '400v':
     case '500v':
     case '700v':
      values = {
        '0' : {value : '', description : 'choose value'},
        '1' : {value : 'otec - syn', description : 'otec - syn'},
        '2' : {value : 'otec - dcera', description : 'otec - dcera'},
        '3' : {value : 'manžel - manželka', description : 'manžel - manželka'},
        '4' : {value : 'matka - syn', description : 'matka - syn'},
        '5' : {value : 'matka - dcera', description : 'matka - dcera'},
        '6' : {value : 'dcera', description : 'dcera'},
        '7' : {value : 'děd - vnuk', description : 'děd - vnuk'},
        '8' : {value : 'děd - vnučka', description : 'děd - vnučka'},
        '9' : {value : 'bába - vnuk', description : 'bába - vnuk'},
        '10' : {value : 'bába - vnučka', description : 'bába - vnučka'},
        '11' : {value : 'bratr - bratr', description : 'bratr - bratr'},
        '12' : {value : 'bratr - sestra', description : 'bratr - sestra'},
        '13' : {value : 'sestra - sestra', description : 'sestra - sestra'},
        '14' : {value : 'strýc/ujec', description : 'strýc/ujec'},
        '15' : {value : 'strýc - synovec/neteř', description : 'strýc - synovec/neteř'},
        '16' : {value : 'teta', description : 'teta'},
        '17' : {value : 'matka', description : 'matka'},
        '18' : {value : 'neteř', description : 'neteř'},
        '19' : {value : 'otec', description : 'otec'},
        '20' : {value : 'syn', description : 'syn'},
        '21' : {value : 'synovec', description : 'synovec'},
        '22' : {value : 'švagr', description : 'švagr'},
        '23' : {value : 'švagrová', description : 'švagrová'},
        '24' : {value : 'tchán', description : 'tchán'},
        '25' : {value : 'tchýně', description : 'tchýně'},
        '26' : {value : 'zeť', description : 'zeť'},
        '27' : {value : 'snacha', description : 'snacha'},
        '28' : {value : 'kmotr', description : 'kmotr'},
        '29' : {value : 'kmotra', description : 'kmotra'},
        '30' : {value : 'ženich', description : 'ženich'},
        '31' : {value : 'nevěsta', description : 'nevěsta'}
      }
      break;
  }

  return values;
}
