import{at as o}from"./sentry.3.5.5.dev18489.js";import"vue";import"./_commonjsHelpers.3.5.5.dev18489.js";function r(i){return i%10<5&&i%10>1&&~~(i/10)%10!==1}function e(i,a,m){var t=i+" ";switch(m){case"m":return a?"minuta":"minutę";case"mm":return t+(r(i)?"minuty":"minut");case"h":return a?"godzina":"godzinę";case"hh":return t+(r(i)?"godziny":"godzin");case"MM":return t+(r(i)?"miesiące":"miesięcy");case"yy":return t+(r(i)?"lata":"lat")}}var n="stycznia_lutego_marca_kwietnia_maja_czerwca_lipca_sierpnia_września_października_listopada_grudnia".split("_"),s="styczeń_luty_marzec_kwiecień_maj_czerwiec_lipiec_sierpień_wrzesień_październik_listopad_grudzień".split("_"),d=/D MMMM/,_=function(i,a){return d.test(a)?n[i.month()]:s[i.month()]};_.s=s;_.f=n;var c={name:"pl",weekdays:"niedziela_poniedziałek_wtorek_środa_czwartek_piątek_sobota".split("_"),weekdaysShort:"ndz_pon_wt_śr_czw_pt_sob".split("_"),weekdaysMin:"Nd_Pn_Wt_Śr_Cz_Pt_So".split("_"),months:_,monthsShort:"sty_lut_mar_kwi_maj_cze_lip_sie_wrz_paź_lis_gru".split("_"),ordinal:function(i){return i+"."},weekStart:1,yearStart:4,relativeTime:{future:"za %s",past:"%s temu",s:"kilka sekund",m:e,mm:e,h:e,hh:e,d:"1 dzień",dd:"%d dni",M:"miesiąc",MM:e,y:"rok",yy:e},formats:{LT:"HH:mm",LTS:"HH:mm:ss",L:"DD.MM.YYYY",LL:"D MMMM YYYY",LLL:"D MMMM YYYY HH:mm",LLLL:"dddd, D MMMM YYYY HH:mm"}};o.locale(c,null,!0);export{c as default};
