(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-8bbc5140"],{"34e1":function(e,a,n){"use strict";n.r(a);n("14d9");var l=n("7a23"),t=n("9062"),i=n.n(t),o=(n("e40d"),n("6605")),r=n("90a7");const u={class:"flex flex-col w-full"},s={class:"info_wrapper_label"},c=["innerHTML"];var d={__name:"JuvenileInfoCard",props:["structure","data","props_for_parents"],setup(e){const a=e,n=Object(l["computed"])(()=>{var e;return null===(e=a.structure)||void 0===e?void 0:e.component}),t=e=>{const n=e.split(".");if(n.length>1){let e=a.data[n[0]];for(let a=1;a<n.length;a++)e=e[n[a]];return e||null}if(e){let n=a.data[e];return n||null}return a.data};return(a,i)=>{var o,r;return Object(l["openBlock"])(),Object(l["createElementBlock"])("div",u,[(Object(l["openBlock"])(!0),Object(l["createElementBlock"])(l["Fragment"],null,Object(l["renderList"])(null===(o=e.structure)||void 0===o?void 0:o.items,(e,a)=>(Object(l["openBlock"])(),Object(l["createElementBlock"])(l["Fragment"],{key:a},[(e.ownFunct?e.ownFunct(t(e.value)):t(e.value))?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",{key:a,class:"info_wrapper"},[Object(l["createElementVNode"])("span",s,Object(l["toDisplayString"])(e.name),1),Object(l["createElementVNode"])("p",{class:"info_wrapper_text",innerHTML:e.ownFunct?e.ownFunct(t(e.value)):t(e.value)},null,8,c)])):Object(l["createCommentVNode"])("",!0)],64))),128)),(Object(l["openBlock"])(),Object(l["createBlock"])(Object(l["resolveDynamicComponent"])(Object(l["unref"])(n)),Object(l["mergeProps"])(null===(r=e.structure)||void 0===r?void 0:r.props,{data:e.props_for_parents}),null,16,["data"]))])}}};const v=d;var m=v,p=n("89ed"),_=n("e19e"),f=n("5779");const b={class:"flex flex-col w-full"},h={class:"info_wrapper_label"},j=["innerHTML"];var g={__name:"ParentInfoCardForPrint",props:["structure","data","class_wrapper"],setup(e){const a=e,n=e=>{const n=e.split(".");if(n.length>1){let e=a.data[n[0]];for(let a=1;a<n.length;a++)e=e[n[a]];return e||null}if(e){let n=a.data[e];return n||null}return a.data};return(a,t)=>(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",b,[(Object(l["openBlock"])(!0),Object(l["createElementBlock"])(l["Fragment"],null,Object(l["renderList"])(e.structure,(a,t)=>(Object(l["openBlock"])(),Object(l["createElementBlock"])(l["Fragment"],{key:t},[n(a.value)?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",{key:t,class:Object(l["normalizeClass"])(e.class_wrapper||"info_wrapper")},[Object(l["createElementVNode"])("span",h,Object(l["toDisplayString"])(a.name),1),Object(l["createElementVNode"])("p",{class:"info_wrapper_text",innerHTML:a.ownFunct?a.ownFunct(n(a.value)):n(a.value)},null,8,j)],2)):Object(l["createCommentVNode"])("",!0)],64))),128))]))}};const y=g;var k=y;const O={class:"flex flex-col gap-2 mt-3"},w={class:"text-xl font-medium"};var x={__name:"ParentInfoCardWrapper",props:["structure","data","class_wrapper"],setup(e){const a=e;return Object(l["watch"])(()=>a.data,()=>console.log(a.data)),(a,n)=>(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",null,[(Object(l["openBlock"])(!0),Object(l["createElementBlock"])(l["Fragment"],null,Object(l["renderList"])(e.data,(a,n)=>(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",{key:n,class:"flex flex-col gap-3"},[Object(l["createElementVNode"])("div",O,[Object(l["createElementVNode"])("h3",w,Object(l["toDisplayString"])(a.parent_type),1),Object(l["createVNode"])(k,{structure:e.structure,data:a,class_wrapper:e.class_wrapper},null,8,["structure","data","class_wrapper"])])]))),128))]))}};const B=x;var F=B;const E={key:1,class:"w-full bg-white rounded-md"},q={class:"flex items-center justify-between py-4 pr-4 none-print"},$={key:0,class:"w-full mx-auto lg:w-full px-6 py-12 flex flex-col items-center gap-4 none-print"},H=["src"],T={class:"flex justify-center w-full overflow-y-auto"},N=["onClick"],V={class:"flex items-center"};var I={__name:"JuvenileInfo",setup(e){var a;const n=Object(o["d"])(),t=Object(l["ref"])([{id:1,text:"Maktabgacha ta'lim",value:"kindergarten"},{id:2,text:"Maktab",value:"school"},{id:3,text:"Kasb-hunar maktabi",value:"vocational_school"},{id:4,text:"Kasb-hunar kolleji",value:"college"},{id:5,text:"Litsey",value:"litsey"},{id:6,text:"Texnikum",value:"texnikum"},{id:7,text:"Maxsus ta’lim",value:"special_education"},{id:8,text:"OTM",value:"university"},{id:9,text:"O‘qimaydi/Ishlamaydi",value:"school_type"},{id:10,text:"Ishlaydi",value:"school_type"}]),u=Object(l["ref"])([{title:"Shaxsiy ma'lumotlar",id:"personal_info"},{title:"Bolaning boquvchisi haqida ma'lumotlar",id:"parent_info"},{title:"Markazga qabul qilish",id:"accept_center_info"},{title:"Taqsimlash",id:"distribute_info"},{title:"Monitoring",id:"monitoring_info"},{title:"Bandligini ta`minlash",id:"employment_info"}]),s=Object(l["ref"])({title:"Shaxsiy ma'lumotlar",id:"personal_info",active:!0}),c=Object(o["c"])(),d=Object(l["ref"])(null),v=Object(l["reactive"])({isNotEmpty:!1,father:{},mother:{}}),b=Object(l["ref"])(!0),{alertThisError:h}=Object(_["a"])(),{fetchJuvenileReportsInfoById:j}=p["a"],g=async()=>{try{var e,a,n,l,t,i,o,r,s,m,p,_,f,g,y,k,O,w,x,B,F,E,q,$,H,T,N,V,I;d.value=await j(c.params.id),d.value.parent_info&&(d.value.parent_info.parents=null===(e=d.value)||void 0===e?void 0:e.parent_info.parents.map(e=>{let a={full_name:`${(null===e||void 0===e?void 0:e.first_name)||""} ${(null===e||void 0===e?void 0:e.last_name)||""} ${(null===e||void 0===e?void 0:e.father_name)||""}`,birth_date:new Date(null===e||void 0===e?void 0:e.birth_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric"}),isAbroad:null!==e&&void 0!==e&&e.is_abroad?"Ha":"Yo'q",isWanted:null!==e&&void 0!==e&&e.is_wanted?"Ha":"Yo'q",...e};return a})),d.value.personal_info&&(d.value.personal_info={...d.value.personal_info,birthDate:(null===(a=d.value.personal_info)||void 0===a?void 0:a.birth_date)&&new Date(null===(n=d.value.personal_info)||void 0===n?void 0:n.birth_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric"}),birth_region:null===(l=d.value.personal_info)||void 0===l||null===(t=l.birth_region)||void 0===t?void 0:t.name,birth_district:null===(i=d.value.personal_info)||void 0===i||null===(o=i.birth_district)||void 0===o?void 0:o.name,passport_type:null===(r=d.value.personal_info)||void 0===r||null===(s=r.passport_type)||void 0===s?void 0:s.name}),d.value.accept_center_info&&(d.value.accept_center_info={...d.value.accept_center_info,determined_location:d.value.accept_center_info.text,arrived_date:(null===(m=d.value)||void 0===m?void 0:m.arrived_date)&&new Date(null===(p=d.value)||void 0===p?void 0:p.arrived_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric"}),filled_date:(null===(_=d.value)||void 0===_||null===(f=_.accept_center_info)||void 0===f||null===(g=f.inspector)||void 0===g?void 0:g.filled_date)&&new Date(null===(y=d.value)||void 0===y||null===(k=y.accept_center_info)||void 0===k||null===(O=k.inspector)||void 0===O?void 0:O.filled_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric",hour:"numeric",minute:"numeric",second:"numeric"})}),d.value.distribute_info&&(d.value.distribute_info={...d.value.distribute_info,distribution_type:null===(w=d.value.distribute_info)||void 0===w||null===(x=w.distribution_type)||void 0===x?void 0:x.text}),d.value.monitoring_info&&(d.value.monitoring_info={...d.value.monitoring_info,monitoring_status:null===(B=d.value.monitoring_info)||void 0===B||null===(F=B.monitoring_status)||void 0===F?void 0:F.text,school_type:null===(E=d.value.monitoring_info)||void 0===E||null===(q=E.school_type)||void 0===q?void 0:q.text,mastery:null===($=d.value.monitoring_info)||void 0===$||null===(H=$.mastery)||void 0===H?void 0:H.text,character:null===(T=d.value.monitoring_info)||void 0===T||null===(N=T.character)||void 0===N?void 0:N.text}),d.value.employment_info&&(d.value.employment_info={...d.value.employment_info,employment_education_type:null===(V=d.value.employment_info)||void 0===V||null===(I=V.employment_education_type)||void 0===I?void 0:I.text}),console.log(d.value),u.value=u.value.map(e=>d.value[e.id]?e:null).filter(e=>e)}catch(D){h(D)}var M,J;d.value&&(null!==(M=d.value)&&void 0!==M&&null!==(J=M.parent)&&void 0!==J&&J.length&&(v.isNotEmpty=!0,v.father=d.value.parent.find(e=>"FATHER"===e.parent_type),v.mother=d.value.parent.find(e=>"MOTHER"===e.parent_type)),b.value=!1)},y=e=>{s.value=e};Object(l["watch"])(()=>c.params.id,async e=>{e&&(b.value=!0,await g(),b.value=!1)},{immediate:!0});const k=Object(l["ref"])([{name:"personal_info",items:[{name:"Ismi:",value:"first_name"},{name:"Familiyasi:",value:"last_name"},{name:"Sharifi:",value:"father_name"},{name:"Tug'ilgan sanasi:",value:"birth_date"},{name:"Tug'ilgan joyi:",value:"birth_region"},{name:"Tug'ilgan tumani:",value:"birth_district"},{name:"Jinsi:",value:"gender",ownFunct:e=>e?"F"===e?"Ayol":"Erkak":e},{name:"JSHSHIR:",value:"pinfl"},{name:"Yashash manzili:",value:"",ownFunct:e=>{var a,n,l,t,i,o,r,u,s,c,v;return e?`${(null===(a=d.value)||void 0===a||null===(n=a.address_info)||void 0===n||null===(l=n.address_region)||void 0===l?void 0:l.name)||""} ${(null===(t=d.value)||void 0===t||null===(i=t.address_info)||void 0===i||null===(o=i.address_district)||void 0===o?void 0:o.name)||""} ${(null===(r=d.value)||void 0===r||null===(u=r.address_info)||void 0===u||null===(s=u.address_mahalla)||void 0===s?void 0:s.name)||""} ${(null===(c=d.value)||void 0===c||null===(v=c.address_info)||void 0===v?void 0:v.address)||""}`:null}},{name:"Hujjat turi:",value:"passport_type"},{name:"Hujjat seria raqami:",value:"passport_seria"},{name:"Horijiy hujjat haqida ma'lumotnoma:",value:"",ownFunct:e=>e?(null===e||void 0===e?void 0:e.reference_type)&&`<a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.reference_type}">(Faylni yuklash)</a>`:null},{name:"Ta'limi:",value:"",ownFunct:e=>{if(e){var a,n,l,i,o;const e=t.value.find(e=>{var a,n;return(null===(a=d.value)||void 0===a?void 0:a.education_info)&&(null===(n=d.value)||void 0===n?void 0:n.education_info[e.value])});return console.log(e),null!==(a=d.value)&&void 0!==a&&a.education_info?(null===(n=d.value)||void 0===n||null===(l=n.education_info[e.value])||void 0===l?void 0:l.name)||(null===(i=d.value)||void 0===i||null===(o=i.education_info[e.value])||void 0===o?void 0:o.text):null}return null}}]},{name:"parent_info",items:[{name:"Bolaning holati:",value:"marital_status.name"}],component:Object(l["markRaw"])(F),props:{structure:[{name:"Boquvchining turi:",value:"parent_type"},{name:"FIO:",value:"",ownFunct:e=>e?`<div class="flex items-center">${null===e||void 0===e?void 0:e.first_name} ${null===e||void 0===e?void 0:e.last_name} ${null!==e&&void 0!==e&&e.father_name?null===e||void 0===e?void 0:e.father_name:""}</div>`:null},{name:"Tug’ilgan sanasi:",value:"birth_date",ownFunct:e=>e?new Date(e).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric"}):null},{name:"Qidiruvdami:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.is_wanted?"Ha":"Yo'q":null},{name:"Chet Eldami:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.is_abroad?"Ha":"Yo'q":null},{name:"Qisqacha ma`lumot:",value:"employment"}],data:null===(a=d.value)||void 0===a?void 0:a.parent_info.parents}},{name:"accept_center_info",items:[{name:"Bolani olib kelish sababi:",value:"reason_bringing_child"},{name:"Bolani olib kelish holati:",value:"sub_reason_bringing_child"},{name:"Holat aniqlangan joyi:",value:"determined_location"},{name:"Olib kelingan sana:",value:"arrived_date"},{name:"Olib kelinishiga asos:",value:"",ownFunct:e=>{var a;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.arrived_reason)||void 0===a?void 0:a.text} <a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.arrived_reason_file}">(Faylni yuklash)</a></div>`:null}},{name:"Profilaktik hisobda turadi:",value:"",ownFunct:e=>{if(e)return e.prophylactic_list?"Ha":"Yo'q"}},{name:"Markazga nechanchi marta kelishi:",value:"center_come_number"},{name:"Tibbiyot D ro‘yxatda turadimi:",value:"",ownFunct:e=>{if(e)return e.is_have_medical_list?`Ha(${(null===e||void 0===e?void 0:e.medical_list.length)&&(null===e||void 0===e?void 0:e.medical_list.join(", "))})`:"Yo'q"}},{name:"Avval RO‘TMda bo‘lganmi:",value:"",ownFunct:e=>{if(e)return e.have_been_in_rotm_reason?"Ha":"Yo'q"}},{name:"Avval ITMda bo‘lganmi:",value:"",ownFunct:e=>{if(e)return e.have_been_in_itm_reason?"Ha":"Yo'q"}},{name:"Markazga olib kelgan xodim:",value:"",ownFunct:e=>{var a,n,l,t;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.inspector)||void 0===a?void 0:a.first_name} ${null===e||void 0===e||null===(n=e.inspector)||void 0===n?void 0:n.last_name} ${null!==e&&void 0!==e&&null!==(l=e.inspector)&&void 0!==l&&l.father_name?null===e||void 0===e||null===(t=e.inspector)||void 0===t?void 0:t.father_name:""}</div>`:null}},{name:"Xizmat olib boruvchi hududi:",value:"",ownFunct:e=>{var a,n;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.inspector)||void 0===a?void 0:a.service_area.region} ${null===e||void 0===e||null===(n=e.inspector)||void 0===n?void 0:n.service_area.district}</div>`:null}},{name:"Yig‘ma jild to‘ldirilgan sana va vaqt:",value:"filled_date"}]},{name:"distribute_info",items:[{name:"Taqsimot turi:",value:"distribution_type"},{name:"Taqsimot asosi:",value:"",ownFunct:e=>{var a;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.basis_distribution)||void 0===a?void 0:a.text} <a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.basis_sending_file}">(Faylni yuklash)</a></div>`:null}},{name:"Boquvchiga o‘quv treyning o‘tkazildimi:",value:"",ownFunct:e=>e?`<div class="flex items-center">${null!==e&&void 0!==e&&e.is_training?"Ha":"Yo'q"} ${null!==e&&void 0!==e&&e.is_training?`<a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.training_file}">(Faylni yuklash)</a>`:""}</div>`:null},{name:"Qiziqishi va qobiliyatlari:",value:"",ownFunct:e=>e?`<a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.skills_hobbies}">(Faylni yuklash)</a>`:null},{name:"Markaz psixoligi va ijtimoiy xodimi tomonidan (Sog'lig'ining ahvoli) o'rganish natijasi:",value:"",ownFunct:e=>e?`<a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.psyhology_condition}">(Faylni yuklash)</a>`:null}]},{name:"monitoring_info",items:[{name:"Monitoring holati:",value:"monitoring_status"},{name:"Muassasa turi:",value:"school_type"},{name:"Mutaxassisligi:",value:"speciality"},{name:"Sinfi/guruhi:",value:"class_group"},{name:"Sinfi/guruhi rahbari:",value:"class_leader"},{name:"Yashash joyi (yotoqxona manzili):",value:"address"},{name:"O‘zlashtirishi:",value:"mastery"},{name:"Hulqi:",value:"character"},{name:"Asoslovchi o‘rganish dalolatnomasi va rasmlar:",value:"",ownFunct:e=>e?`<a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.deed_and_pictures}">(Faylni yuklash)</a>`:null},{name:"MJtKning 47-moddasi bilan chora ko‘rildimi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.file_action_been_taken?`<span>Ha</span> <a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.psyhology_condition}">(Faylni yuklash)</a>`:"Yo'q":null}]},{name:"employment_info",items:[{name:"Ta’lim muassasasiga hujjat topshirganmi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.is_applied_document?"Ha":"Yo'q":null},{name:"Ta’lim muassasa turi:",value:"employment_education_type"},{name:"Ta’lim muassasa nomi:",value:"school_name"},{name:"Ta’lim yo‘nalishi:",value:"education_direction"},{name:"Mutaxassisligi:",value:"employment_speciality"},{name:"Talim muassasasiga qabul qilinganmi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.is_accepted_to_school?"Ha":"Yo'q":null},{name:"Qabul qilingan talim muassasasi:",value:"accepted_school",ownFunct:e=>e||"-"},{name:"Asos:",value:"",ownFunct:e=>e?`<a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.school_applied_file}">(Faylni yuklash)</a>`:null},{name:"Harbiy xizmatga yuborilganligi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.military_conscripted_file?`<span>Ha</span> <a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.military_conscripted_file}">(Faylni yuklash)</a>`:"Yo'q":null},{name:"Bandligi taminlanganlinganmi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.employment_file?`<span>Ha</span> <a class="text-blue-500 ml-2" target="_blank" href="${null===e||void 0===e?void 0:e.employment_file}">(Faylni yuklash)</a>`:"Yo'q":null},{name:"Mahalla va oilani qo'llab quvvatlash bo'limi tamonidan biriktirilgan murabbiy FISH:",value:"neighborhood_coach"},{name:"Profilaktika inspektori FISH:",value:"employment_inspector"}]}]),O=()=>{n.push({name:"teenager-info-print",params:{id:c.params.id}})};return(e,a)=>{var n,t,o,c;return Object(l["openBlock"])(),Object(l["createElementBlock"])(l["Fragment"],null,[b.value?(Object(l["openBlock"])(),Object(l["createBlock"])(Object(l["unref"])(i.a),{key:0,active:b.value,"onUpdate:active":a[0]||(a[0]=e=>b.value=e),"can-cancel":!1,"is-full-page":!0,color:"#4785FE",loader:"dots"},null,8,["active"])):Object(l["createCommentVNode"])("",!0),!b.value&&d.value?(Object(l["openBlock"])(),Object(l["createElementBlock"])("section",E,[Object(l["createElementVNode"])("div",q,[Object(l["createVNode"])(Object(l["unref"])(r["a"]),null,{default:Object(l["withCtx"])(()=>[Object(l["createTextVNode"])(" Bola haqida ma'lumot ")]),_:1}),Object(l["createElementVNode"])("button",{class:"text-white bg-[#4785FE] px-[30px] py-[8px] flex gap-[13px] item-center rounded-[6px]",onClick:O},[Object(l["createTextVNode"])(" Yuklab olish "),Object(l["createVNode"])(Object(l["unref"])(f["a"]),{icon:"bi:download",class:"text-white w-[18px] h-[18px]"})])]),d.value?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",$,[Object(l["createElementVNode"])("img",{src:(null===(n=d.value)||void 0===n||null===(t=n.personal_info)||void 0===t?void 0:t.photo)||"https://images.unsplash.com/photo-1608734265656-f035d3e7bcbf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",class:"max-w-xs w-full h-auto"},null,8,H),Object(l["createElementVNode"])("div",T,[(Object(l["openBlock"])(!0),Object(l["createElementBlock"])(l["Fragment"],null,Object(l["renderList"])(u.value,e=>{var a;return Object(l["openBlock"])(),Object(l["createElementBlock"])("button",{key:e.id,class:Object(l["normalizeClass"])(["px-[15px] py-[10px] text-sm grow border-b-2 flex-shrink-0",e.id===(null===(a=s.value)||void 0===a?void 0:a.id)?"text-[#4785FE] bg-white border-[#4785FE]":"text-[#0B0B0B] border-[#EBEBEB]"]),onClick:a=>y(e)},[Object(l["createElementVNode"])("span",V,Object(l["toDisplayString"])(e.title),1)],10,N)}),128))]),Object(l["createVNode"])(m,{props_for_parents:null===(o=d.value)||void 0===o||null===(c=o.parent_info)||void 0===c?void 0:c.parents,data:d.value[s.value.id],structure:k.value.find(e=>e.name===s.value.id)},null,8,["props_for_parents","data","structure"])])):Object(l["createCommentVNode"])("",!0)])):Object(l["createCommentVNode"])("",!0)],64)}}};const M=I;a["default"]=M},"89ed":function(e,a,n){"use strict";var l=n("451b");const t={async fetchJuvenileById(e){const{data:a}=await l["a"].get(`/api/juvenile/juveniles/${e}/`);return a},async fetchJuvenileInfoDetailById(e){const{data:a}=await l["a"].get(`/api/juvenile/juveniles/${e}/juvenile_info_detail/`);return a},async fetchJuvenilesList(e={}){return(await l["a"].get("/api/juvenile/juveniles/",{params:e})).data},async fetchJuvenileReportsList(e={}){return(await l["a"].get("/api/juvenile/reports/",{params:{...e}})).data},async fetchJuvenileReportById(e){const{data:a}=await l["a"].get(`/api/juvenile/is_filled/${e}/`);return a},async fetchJuvenileReportsInfoById(e){const{data:a}=await l["a"].get("/api/juvenile/reports/"+e);return a},async fetchAcceptedJuvenilesInfo(e){const{data:a}=await l["a"].get(`/api/juvenile/accepted_for_edit/${e}/`);return a},async acceptJuvenileToCenter(e,a){return await l["a"].post("/api/juvenile/juveniles/accept_juvenile/",a,{params:{juvenile_id:e}})},async createAvailableJuvenile(e){return await l["a"].post("/api/juvenile/juveniles/create_available_juvenile/?juvenile_id="+e)},async updateJuvenile(e,a){return await l["a"].put("/api/juvenile/juveniles/"+a,e)},async createJuvenilePersonalInfo(e){return await l["a"].post("/api/juvenile/juveniles/",e)},async createJuvenileAddressInfo(e,a){return await l["a"].post(`/api/juvenile/juveniles/${e}/juvenile_addressinfo_create_or_update/`,a)},async createJuvenileEducationInfo(e,a){return await l["a"].post(`/api/juvenile/juveniles/${e}/juvenile_educationinfo_create_or_update/`,a)},async getDeterminedJuvenilesList(e){const a=(await l["a"].get("/api/juvenile/juveniles/incomplete_juveniles/",{params:e})).data,n=a.results.map(e=>{var a,n,l,t;return{birth_date:null===(a=e.personal_info)||void 0===a?void 0:a.birth_date,father_name:null===(n=e.personal_info)||void 0===n?void 0:n.father_name,first_name:null===(l=e.personal_info)||void 0===l?void 0:l.first_name,last_name:null===(t=e.personal_info)||void 0===t?void 0:t.last_name,...e}});return{...a,results:n}},async getNotDefinedJuvenilesList(e){return(await l["a"].get("/api/juvenile/juveniles/unidentified_juveniles",{params:e})).data},async delete_incomplete_juvenile(e){return await l["a"].delete(`/api/juvenile/juveniles/${e}/delete_incomplete_juvenile/`)},async delete_unidentified_juvenile(e){return await l["a"].delete(`/api/juvenile/juveniles/${e}/delete_unidentified_juvenile/`)}};a["a"]=t},"90a7":function(e,a,n){"use strict";var l=n("7a23");const t={class:"flex items-center gap-5"};function i(e,a,n,i,o,r){const u=Object(l["resolveComponent"])("GoBackBtn");return Object(l["openBlock"])(),Object(l["createElementBlock"])("div",t,[Object(l["createVNode"])(u),Object(l["createElementVNode"])("h1",null,[Object(l["renderSlot"])(e.$slots,"default")])])}const o=Object(l["createElementVNode"])("svg",{xmlns:"http://www.w3.org/2000/svg",class:"h-6 w-6 text-blue-400",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(l["createElementVNode"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M11 17l-5-5m0 0l5-5m-5 5h12"})],-1),r=[o];function u(e,a,n,t,i,o){return Object(l["openBlock"])(),Object(l["createElementBlock"])("button",{class:"clickEffectBtn px-4 py-2",onClick:a[0]||(a[0]=a=>e.$router.back())},r)}var s={name:"GoBackBtn"},c=n("d959"),d=n.n(c);const v=d()(s,[["render",u]]);var m=v,p={name:"PageTitleWithGoBackButton",components:{GoBackBtn:m}};const _=d()(p,[["render",i]]);a["a"]=_},b7a4:function(e,a,n){"use strict";n.d(a,"a",(function(){return t}));var l=n("0180");function t(){const e=Object(l["b"])();function a(a,n=["success","error","danger","info"][0]){e(a,{type:n})}return{alertIt:a}}},e19e:function(e,a,n){"use strict";n.d(a,"a",(function(){return t}));var l=n("b7a4");function t(){const{alertIt:e}=Object(l["a"])(),a=a=>{var n,l,t,i,o,r,u,s,c,d,v;if(console.log({error:a},"UseErrorAlert"),"string"===typeof(null===a||void 0===a||null===(n=a.response)||void 0===n||null===(l=n.data)||void 0===l?void 0:l.message))e(null===a||void 0===a||null===(d=a.response)||void 0===d||null===(v=d.data)||void 0===v?void 0:v.message,"error");else if(null!==a&&void 0!==a&&null!==(t=a.response)&&void 0!==t&&t.data&&"string"!==typeof(null===a||void 0===a||null===(i=a.response)||void 0===i?void 0:i.data)&&null!==a&&void 0!==a&&null!==(o=a.response)&&void 0!==o&&null!==(r=o.data)&&void 0!==r&&r.messages)Object.values(a.response.data.messages).map(a=>{null!==a&&void 0!==a&&a.message&&e(a.message,"error")});else if(Array.isArray(null===a||void 0===a||null===(u=a.response)||void 0===u?void 0:u.data)){var m;null===a||void 0===a||null===(m=a.response)||void 0===m||m.data.map(a=>{e(a,"error")})}else null!==a&&void 0!==a&&null!==(s=a.response)&&void 0!==s&&s.data&&400===(null===a||void 0===a||null===(c=a.response)||void 0===c?void 0:c.status)?Object.values(a.response.data).map(a=>{"string"==typeof a?e(a,"error"):a.map(a=>e(a,"error"))}):e("Server bilan bog'liq xatolik yuz berdi.","error")};return{alertThisError:a}}}}]);
//# sourceMappingURL=chunk-8bbc5140.faa291c7.js.map