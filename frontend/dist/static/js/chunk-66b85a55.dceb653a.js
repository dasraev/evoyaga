(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-66b85a55"],{"0a49":function(e,a,t){},6139:function(e,a,t){"use strict";t("0a49")},"714b":function(e,a,t){"use strict";var n=t("7a23");const i={class:"flex flex-col w-full"},l={class:"info_wrapper_label_for_print"},o=["innerHTML"];var r={__name:"PrintList",props:["structure","data","props_for_parents"],setup(e){const a=e,t=Object(n["computed"])(()=>{var e;return null===(e=a.structure)||void 0===e?void 0:e.component}),r=e=>{const t=e.split(".");if(t.length>1){let e=a.data[t[0]];for(let a=1;a<t.length;a++)e=e[t[a]];return e||null}if(e){let t=a.data[e];return t||null}return a.data};return(a,u)=>{var s,c;return Object(n["openBlock"])(),Object(n["createElementBlock"])("div",i,[(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(null===(s=e.structure)||void 0===s?void 0:s.items,(e,a)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])(n["Fragment"],{key:a},[r(e.value)?(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",{key:a,class:"info_wrapper_for_print"},[Object(n["createElementVNode"])("span",l,Object(n["toDisplayString"])(e.name),1),Object(n["createElementVNode"])("p",{class:"info_wrapper_text_for_print",innerHTML:e.ownFunct?e.ownFunct(r(e.value)):r(e.value)},null,8,o)])):Object(n["createCommentVNode"])("",!0)],64))),128)),(Object(n["openBlock"])(),Object(n["createBlock"])(Object(n["resolveDynamicComponent"])(Object(n["unref"])(t)),Object(n["mergeProps"])(null===(c=e.structure)||void 0===c?void 0:c.props,{data:e.props_for_parents}),null,16,["data"]))])}}};const u=r;var s=u;const c={class:"flex flex-col gap-5"},d={class:"w-[3cm] h-[4cm] overflow-hidden absolute right-[2cm] top-[2cm]"},v=["src"],m={class:"flex flex-col gap-2 w-full"},p={class:"text-lg font-bold"};var _={__name:"PrintWrapper",props:["structure","data","tabs"],setup(e){return(a,t)=>{var i,l;return Object(n["openBlock"])(),Object(n["createElementBlock"])("div",c,[Object(n["createElementVNode"])("div",d,[Object(n["createElementVNode"])("img",{src:(null===(i=e.data)||void 0===i||null===(l=i.personal_info)||void 0===l?void 0:l.photo)||"https://images.unsplash.com/photo-1608734265656-f035d3e7bcbf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",class:"w-full h-auto object-cover"},null,8,v)]),(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(e.structure,(a,t)=>{var i,l,o;return Object(n["openBlock"])(),Object(n["createElementBlock"])("div",{key:t,class:"flex justify-between gap-6 w-full"},[Object(n["createElementVNode"])("div",m,[Object(n["createElementVNode"])("h2",p,Object(n["toDisplayString"])(null===(i=e.tabs.find(e=>e.id===a.name))||void 0===i?void 0:i.title),1),Object(n["createVNode"])(s,{structure:a,data:e.data[a.name],props_for_parents:null===(l=e.data)||void 0===l||null===(o=l.parent_info)||void 0===o?void 0:o.parents},null,8,["structure","data","props_for_parents"])])])}),128))])}}};const b=_;a["a"]=b},"89ed":function(e,a,t){"use strict";var n=t("451b");const i={async fetchJuvenileById(e){const{data:a}=await n["a"].get(`/api/juvenile/juveniles/${e}/`);return a},async fetchJuvenileInfoDetailById(e){const{data:a}=await n["a"].get(`/api/juvenile/juveniles/${e}/juvenile_info_detail/`);return a},async fetchJuvenilesList(e={}){return(await n["a"].get("/api/juvenile/juveniles/",{params:e})).data},async fetchJuvenileReportsList(e={}){return(await n["a"].get("/api/juvenile/reports/",{params:{...e}})).data},async fetchJuvenileReportById(e){const{data:a}=await n["a"].get(`/api/juvenile/is_filled/${e}/`);return a},async fetchJuvenileReportsInfoById(e){const{data:a}=await n["a"].get("/api/juvenile/reports/"+e);return a},async fetchAcceptedJuvenilesInfo(e){const{data:a}=await n["a"].get(`/api/juvenile/accepted_for_edit/${e}/`);return a},async acceptJuvenileToCenter(e,a){return await n["a"].post("/api/juvenile/juveniles/accept_juvenile/",a,{params:{juvenile_id:e}})},async createAvailableJuvenile(e){return await n["a"].post("/api/juvenile/juveniles/create_available_juvenile/?juvenile_id="+e)},async updateJuvenile(e,a){return await n["a"].put("/api/juvenile/juveniles/"+a,e)},async createJuvenilePersonalInfo(e){return await n["a"].post("/api/juvenile/juveniles/",e)},async createJuvenileAddressInfo(e,a){return await n["a"].post(`/api/juvenile/juveniles/${e}/juvenile_addressinfo_create_or_update/`,a)},async createJuvenileEducationInfo(e,a){return await n["a"].post(`/api/juvenile/juveniles/${e}/juvenile_educationinfo_create_or_update/`,a)},async getDeterminedJuvenilesList(e){const a=(await n["a"].get("/api/juvenile/juveniles/incomplete_juveniles/",{params:e})).data,t=a.results.map(e=>({birth_date:e.personal_info.birth_date,father_name:e.personal_info.father_name,first_name:e.personal_info.first_name,last_name:e.personal_info.last_name,...e}));return{...a,results:t}},async getNotDefinedJuvenilesList(e){return(await n["a"].get("/api/juvenile/juveniles/unidentified_juveniles",{params:e})).data},async delete_incomplete_juvenile(e){return await n["a"].delete(`/api/juvenile/juveniles/${e}/delete_incomplete_juvenile/`)},async delete_unidentified_juvenile(e){return await n["a"].delete(`/api/juvenile/juveniles/${e}/delete_unidentified_juvenile/`)}};a["a"]=i},"8cd8":function(e,a,t){"use strict";t.r(a);var n=t("7a23"),i=t("9062"),l=t.n(i),o=(t("e40d"),t("6605")),r=t("714b"),u=t("89ed"),s=t("e19e");const c=e=>(Object(n["pushScopeId"])("data-v-005f06fa"),e=e(),Object(n["popScopeId"])(),e),d={class:"w-full"},v=c(()=>Object(n["createElementVNode"])("th",{class:"w-28 text-left text-xs px-0.5"},"T/r",-1)),m=["onClick"],p={class:"w-28 px-0.5"},_=["title"],b={class:"text-xs"};var f={__name:"TableForParentPrint",props:{headers:{type:Array,default:()=>[{text:"Dessert (100g serving)",align:"start",sortable:!1,value:"name"},{text:"Calories",value:"calories"},{text:"Fat (g)",value:"fat"},{text:"Carbs (g)",value:"carbs"},{text:"Protein (g)",value:"protein"},{text:"Iron (%)",value:"iron"}]},data:{type:Array},loading:{type:Boolean},rowsClass:{type:String},tableClass:{type:String},class:{type:String},headerClass:{type:String},isCheckbox:{type:Boolean,default:()=>!1},indicator:{type:Boolean,default:()=>!1},classBody:{type:String},blured:{type:String},reRender:{type:String}},emits:["click","check-header"],setup(e,{emit:a}){const t=e;Object(n["watch"])(()=>t.reRender,e=>{const a=document.querySelectorAll('input[type="checkbox"]');a.forEach(e=>{e.checked=!1})});const i=(e,a)=>Array.isArray(a.value)?e[a.value[0]][a.value[1]]:e[a.value];return(l,o)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",{class:Object(n["normalizeClass"])(["data-table",t.class])},[Object(n["createElementVNode"])("table",d,[Object(n["createElementVNode"])("thead",null,[Object(n["createElementVNode"])("tr",null,[v,(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(e.headers,e=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("th",{class:Object(n["normalizeClass"])(["text-left text-xs px-0.5",[e.class,e.value]]),key:e.value},Object(n["toDisplayString"])(e.text),3))),128))])]),Object(n["createElementVNode"])("tbody",{class:Object(n["normalizeClass"])([e.classBody,{ischeckbox:e.isCheckbox}])},[(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(e.data,(t,o)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("tr",{class:Object(n["normalizeClass"])([e.rowsClass,t[e.blured]?"blured":""]),onClick:e=>a("click",t),key:o},[Object(n["createElementVNode"])("td",p,Object(n["toDisplayString"])(o+1),1),(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(e.headers,e=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("td",{key:e.value,title:i(t,e),class:Object(n["normalizeClass"])([e.class,e.value," px-0.5"])},[Object(n["renderSlot"])(l.$slots,e.value,{items:{index:o,item:t,text:i(t,e),value:e.value}},()=>[Object(n["createElementVNode"])("span",b,Object(n["toDisplayString"])(i(t,e)),1)])],10,_))),128))],10,m))),128))],2)])],2))}},j=(t("6139"),t("d959")),h=t.n(j);const g=h()(f,[["__scopeId","data-v-965e5d88"]]);var y=g;t("a18c");const O={key:1,class:"w-full bg-white rounded-md pt-[2cm] pl-[3cm] pr-[2cm] pb-[2cm]"};var k={__name:"JuvenileInfoForPrint",setup(e){const a=Object(n["ref"])([{name:"personal_info",items:[{name:"Ismi:",value:"first_name"},{name:"Familiyasi:",value:"last_name"},{name:"Sharifi:",value:"father_name"},{name:"Tug'ilgan sanasi:",value:"birth_date"},{name:"Tug'ilgan joyi:",value:"birth_region"},{name:"Tug'ilgan tumani:",value:"birth_district"},{name:"Jinsi:",value:"gender",ownFunct:e=>e?"F"===e?"Ayol":"Erkak":e},{name:"JSHSHIR:",value:"pinfl"},{name:"Yashash manzili:",value:"",ownFunct:e=>{var a,t;return console.log(e),e?null===(a=d.value)||void 0===a||null===(t=a.address_info)||void 0===t?void 0:t.address:e}},{name:"Hujjat turi:",value:"passport_type"},{name:"Hujjat seria raqami:",value:"passport_seria"},{name:"Ta'limi:",value:"",ownFunct:e=>{if(e){var a,n,i;const e=t.value.find(e=>{var a,t;return(null===(a=d.value)||void 0===a?void 0:a.education_info)&&(null===(t=d.value)||void 0===t?void 0:t.education_info[e.value])});return null!==(a=d.value)&&void 0!==a&&a.education_info?null===(n=d.value)||void 0===n||null===(i=n.education_info[e.value])||void 0===i?void 0:i.name:null}return""}}]},{name:"accept_center_info",items:[{name:"Bolani olib kelish sababi:",value:"reason_bringing_child"},{name:"Bolani olib kelish holati:",value:"sub_reason_bringing_child"},{name:"Holat aniqlangan joyi:",value:"determined_location"},{name:"Olib kelingan sana:",value:"arrived_date"},{name:"Olib kelinishiga asos:",value:"",ownFunct:e=>{var a;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.arrived_reason)||void 0===a?void 0:a.text}</div>`:null}},{name:"Profilaktik hisobda turadi:",value:"",ownFunct:e=>{if(e)return e.prophylactic_list?"Ha":"Yo'q"}},{name:"Markazga nechanchi marta kelishi:",value:"center_come_number"},{name:"Tibbiyot D ro‘yxatda turadimi:",value:"",ownFunct:e=>{if(e)return e.is_have_medical_list?`Ha(${(null===e||void 0===e?void 0:e.medical_list.length)&&(null===e||void 0===e?void 0:e.medical_list.join(", "))})`:"Yo'q"}},{name:"Avval RO‘TMda bo‘lganmi:",value:"",ownFunct:e=>{if(e)return e.have_been_in_rotm_reason?"Ha":"Yo'q"}},{name:"Avval ITMda bo‘lganmi:",value:"",ownFunct:e=>{if(e)return e.have_been_in_itm_reason?"Ha":"Yo'q"}},{name:"Markazga olib kelgan xodim:",value:"",ownFunct:e=>{var a,t,n,i;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.inspector)||void 0===a?void 0:a.first_name} ${null===e||void 0===e||null===(t=e.inspector)||void 0===t?void 0:t.last_name} ${null!==e&&void 0!==e&&null!==(n=e.inspector)&&void 0!==n&&n.father_name?null===e||void 0===e||null===(i=e.inspector)||void 0===i?void 0:i.father_name:""}</div>`:null}},{name:"Xizmat olib boruvchi hududi:",value:"",ownFunct:e=>{var a,t;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.inspector)||void 0===a?void 0:a.service_area.region} ${null===e||void 0===e||null===(t=e.inspector)||void 0===t?void 0:t.service_area.district}</div>`:null}},{name:"Yig‘ma jild to‘ldirilgan sana va vaqt:",value:"filled_date"}]},{name:"distribute_info",items:[{name:"Taqsimot turi:",value:"distribution_type"},{name:"Taqsimot asosi:",value:"",ownFunct:e=>{var a;return e?`<div class="flex items-center">${null===e||void 0===e||null===(a=e.basis_distribution)||void 0===a?void 0:a.text}</div>`:null}},{name:"Boquvchiga o‘quv treyning o‘tkazildimi:",value:"",ownFunct:e=>e?`<div class="flex items-center">${null!==e&&void 0!==e&&e.is_training?"Ha":"Yo'q"}</div>`:null}]},{name:"monitoring_info",items:[{name:"Monitoring holati:",value:"monitoring_status"},{name:"Muassasa turi:",value:"school_type"},{name:"Mutaxassisligi:",value:"speciality"},{name:"Sinfi/guruhi:",value:"class_group"},{name:"Sinfi/guruhi rahbari:",value:"class_leader"},{name:"Yashash joyi (yotoqxona manzili):",value:"address"},{name:"O‘zlashtirishi:",value:"mastery"},{name:"Hulqi:",value:"character"},{name:"MJtKning 47-moddasi bilan chora ko‘rildimi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.file_action_been_taken?"Ha":"Yo'q":null}]},{name:"employment_info",items:[{name:"Ta’lim muassasasiga hujjat topshirganmi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.is_applied_document?"Ha":"Yo'q":null},{name:"Ta’lim muassasa turi:",value:"employment_education_type"},{name:"Ta’lim muassasa nomi:",value:"school_name"},{name:"Ta’lim yo‘nalishi:",value:"education_direction"},{name:"Mutaxassisligi:",value:"employment_speciality"},{name:"Talim muassasasiga qabul qilinganmi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.is_accepted_to_school?"Ha":"Yo'q":null},{name:"Qabul qilingan talim muassasasi:",value:"accepted_school",ownFunct:e=>e||"-"},{name:"Harbiy xizmatga yuborilganligi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.military_conscripted_file?"Ha":"Yo'q":null},{name:"Bandligi taminlanganlinganmi:",value:"",ownFunct:e=>e?null!==e&&void 0!==e&&e.employment_file?"Ha":"Yo'q":null},{name:"Mahalla va oilani qo'llab quvvatlash bo'limi tamonidan biriktirilgan murabbiy FISH:",value:"neighborhood_coach"},{name:"Profilaktika inspektori FISH:",value:"employment_inspector"}]},{name:"parent_info",component:Object(n["markRaw"])(y),props:{headers:[{text:"Boquvchining turi",value:"parent_type"},{text:"FIO",value:"full_name"},{text:"Tug’ilgan sanasi",value:"birthDate"},{text:"Qidiruvdami",value:"isWanted"},{text:"Chet Eldami",value:"isAbroad"},{text:"Qisqacha ma`lumot",value:"employment"}],class_wrapper:"info_wrapper_for_print"}}]),t=Object(n["ref"])([{id:1,text:"Maktabgacha ta'lim",value:"kindergarten"},{id:2,text:"Maktab",value:"school"},{id:3,text:"Kasb-hunar maktabi",value:"vocational_school"},{id:4,text:"Kasb-hunar kolleji",value:"college"},{id:5,text:"Litsey",value:"litsey"},{id:6,text:"Texnikum",value:"texnikum"},{id:7,text:"Maxsus ta’lim",value:"special_education"},{id:8,text:"OTM",value:"university"},{id:9,text:"O‘qimaydi/Ishlamaydi"},{id:10,text:"Ishlaydi"}]),i=Object(n["ref"])([{title:"Shaxsiy ma'lumotlar",id:"personal_info"},{title:"Bolaning boquvchisi haqida ma'lumotlar",id:"parent_info"},{title:"Markazga qabul qilish",id:"accept_center_info"},{title:"Taqsimlash",id:"distribute_info"},{title:"Monitoring",id:"monitoring_info"},{title:"Bandligini ta`minlash",id:"employment_info"}]),c=(Object(n["ref"])({title:"Shaxsiy ma'lumotlar",id:"personal_info",active:!0}),Object(o["c"])()),d=Object(n["ref"])(null),v=Object(n["reactive"])({isNotEmpty:!1,father:{},mother:{}}),m=Object(n["ref"])(!0),{alertThisError:p}=Object(s["a"])(),{fetchJuvenileReportsInfoById:_}=u["a"],b=async()=>{try{var e,t,n,i,l,o,r,u,s,b,f,j,h,g,y,O,k,x,w,B,E,q,F,S,H,T,I,D,M;d.value=await _(c.params.id),d.value.parent_info&&(d.value.parent_info.parents=null===(e=d.value)||void 0===e?void 0:e.parent_info.parents.map(e=>{let a={full_name:`${(null===e||void 0===e?void 0:e.first_name)||""} ${(null===e||void 0===e?void 0:e.last_name)||""} ${(null===e||void 0===e?void 0:e.father_name)||""}`,birthDate:new Date(null===e||void 0===e?void 0:e.birth_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric"}),isAbroad:null!==e&&void 0!==e&&e.is_abroad?"Ha":"Yo'q",isWanted:null!==e&&void 0!==e&&e.is_wanted?"Ha":"Yo'q",...e};return a})),d.value.personal_info&&(d.value.personal_info={...d.value.personal_info,birth_date:(null===(t=d.value.personal_info)||void 0===t?void 0:t.birth_date)&&new Date(null===(n=d.value.personal_info)||void 0===n?void 0:n.birth_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric"}),birth_region:null===(i=d.value.personal_info)||void 0===i||null===(l=i.birth_region)||void 0===l?void 0:l.name,birth_district:null===(o=d.value.personal_info)||void 0===o||null===(r=o.birth_district)||void 0===r?void 0:r.name,passport_type:null===(u=d.value.personal_info)||void 0===u||null===(s=u.passport_type)||void 0===s?void 0:s.name}),d.value.accept_center_info&&(d.value.accept_center_info={...d.value.accept_center_info,determined_location:d.value.accept_center_info.text,arrived_date:(null===(b=d.value)||void 0===b?void 0:b.arrived_date)&&new Date(null===(f=d.value)||void 0===f?void 0:f.arrived_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric"}),filled_date:(null===(j=d.value)||void 0===j||null===(h=j.accept_center_info)||void 0===h||null===(g=h.inspector)||void 0===g?void 0:g.filled_date)&&new Date(null===(y=d.value)||void 0===y||null===(O=y.accept_center_info)||void 0===O||null===(k=O.inspector)||void 0===k?void 0:k.filled_date).toLocaleDateString("ru-Ru",{year:"numeric",month:"numeric",day:"numeric",hour:"numeric",minute:"numeric",second:"numeric"})}),d.value.distribute_info&&(d.value.distribute_info={...d.value.distribute_info,distribution_type:null===(x=d.value.distribute_info)||void 0===x||null===(w=x.distribution_type)||void 0===w?void 0:w.text}),d.value.monitoring_info&&(d.value.monitoring_info={...d.value.monitoring_info,monitoring_status:null===(B=d.value.monitoring_info)||void 0===B||null===(E=B.monitoring_status)||void 0===E?void 0:E.text,school_type:null===(q=d.value.monitoring_info)||void 0===q||null===(F=q.school_type)||void 0===F?void 0:F.text,mastery:null===(S=d.value.monitoring_info)||void 0===S||null===(H=S.mastery)||void 0===H?void 0:H.text,character:null===(T=d.value.monitoring_info)||void 0===T||null===(I=T.character)||void 0===I?void 0:I.text}),d.value.employment_info&&(d.value.employment_info={...d.value.employment_info,employment_education_type:null===(D=d.value.employment_info)||void 0===D||null===(M=D.employment_education_type)||void 0===M?void 0:M.text}),a.value=a.value.map(e=>d.value[e.name]?e:null).filter(e=>e)}catch(N){p(N)}var J,C;d.value&&(null!==(J=d.value)&&void 0!==J&&null!==(C=J.parent)&&void 0!==C&&C.length&&(v.isNotEmpty=!0,v.father=d.value.parent.find(e=>"FATHER"===e.parent_type),v.mother=d.value.parent.find(e=>"MOTHER"===e.parent_type)),m.value=!1)};return Object(n["watch"])(()=>c.params.id,async e=>{e&&(m.value=!0,await b(),m.value=!1)},{immediate:!0}),Object(n["onMounted"])(async()=>{await b(),setTimeout(()=>{window.print()},1e3)}),(e,t)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])(n["Fragment"],null,[m.value?(Object(n["openBlock"])(),Object(n["createBlock"])(Object(n["unref"])(l.a),{key:0,active:m.value,"onUpdate:active":t[0]||(t[0]=e=>m.value=e),"can-cancel":!1,"is-full-page":!0,color:"#4785FE",loader:"dots"},null,8,["active"])):Object(n["createCommentVNode"])("",!0),!m.value&&d.value?(Object(n["openBlock"])(),Object(n["createElementBlock"])("section",O,[Object(n["createVNode"])(r["a"],{structure:a.value,data:d.value,tabs:i.value},null,8,["structure","data","tabs"])])):Object(n["createCommentVNode"])("",!0)],64))}};const x=k;a["default"]=x},b7a4:function(e,a,t){"use strict";t.d(a,"a",(function(){return i}));var n=t("0180");function i(){const e=Object(n["b"])();function a(a,t=["success","error","danger","info"][0]){e(a,{type:t})}return{alertIt:a}}},e19e:function(e,a,t){"use strict";t.d(a,"a",(function(){return i}));var n=t("b7a4");function i(){const{alertIt:e}=Object(n["a"])(),a=a=>{var t,n,i,l,o,r,u,s,c,d,v;if(console.log({error:a},"UseErrorAlert"),"string"===typeof(null===a||void 0===a||null===(t=a.response)||void 0===t||null===(n=t.data)||void 0===n?void 0:n.message))e(null===a||void 0===a||null===(d=a.response)||void 0===d||null===(v=d.data)||void 0===v?void 0:v.message,"error");else if(null!==a&&void 0!==a&&null!==(i=a.response)&&void 0!==i&&i.data&&"string"!==typeof(null===a||void 0===a||null===(l=a.response)||void 0===l?void 0:l.data)&&null!==a&&void 0!==a&&null!==(o=a.response)&&void 0!==o&&null!==(r=o.data)&&void 0!==r&&r.messages)Object.values(a.response.data.messages).map(a=>{null!==a&&void 0!==a&&a.message&&e(a.message,"error")});else if(Array.isArray(null===a||void 0===a||null===(u=a.response)||void 0===u?void 0:u.data)){var m;null===a||void 0===a||null===(m=a.response)||void 0===m||m.data.map(a=>{e(a,"error")})}else null!==a&&void 0!==a&&null!==(s=a.response)&&void 0!==s&&s.data&&400===(null===a||void 0===a||null===(c=a.response)||void 0===c?void 0:c.status)?Object.values(a.response.data).map(a=>{"string"==typeof a?e(a,"error"):a.map(a=>e(a,"error"))}):e("Server bilan bog'liq xatolik yuz berdi.","error")};return{alertThisError:a}}}}]);
//# sourceMappingURL=chunk-66b85a55.dceb653a.js.map