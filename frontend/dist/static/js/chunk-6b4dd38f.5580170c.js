(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6b4dd38f"],{"1a02":function(e,t,a){"use strict";a.d(t,"a",(function(){return r}));var n=a("7a23"),i=a("4b59");function r(){const e=Object(n["ref"])([]),t=async()=>{const{data:t}=await i["a"].fetchSchoolTypes();e.value=t};return Object(n["onMounted"])(async()=>{await t()}),{schoolTypes:e}}},2145:function(e,t,a){"use strict";a.r(t);var n=a("7a23"),i=a("9062"),r=a.n(i),c=(a("e40d"),a("14d9"),a("5779"));const s={class:"min-w-full table-auto text-sm xl:text-md"},l={class:"bg-white border-b border-gray-300 text-gray-400"},o=Object(n["createElementVNode"])("th",{class:"w-20 py-4"}," T/r ",-1),u=Object(n["createElementVNode"])("th",{class:"text-left py-4 pl-3"}," F.I.Sh ",-1),d=Object(n["createElementVNode"])("th",{class:"py-4 pl-3"}," Markazga qabul qilingan ",-1),p=Object(n["createElementVNode"])("th",{class:"py-4 pl-3"}," Holati ",-1),b=Object(n["createElementVNode"])("th",{class:"py-4 pl-3"}," Taqsimlagan ",-1),v=Object(n["createElementVNode"])("th",{class:"py-4"}," Ma'lumot ",-1),g=Object(n["createElementVNode"])("th",{class:"py-4"},null,-1),j=Object(n["createElementVNode"])("th",{class:"py-4"},null,-1),y={class:"w-20 py-4"},m={class:"text-center"},f={class:"py-4 overflow-hidden overflow-ellipsis"},h={class:"flex items-center"},O={class:"text-center px-3 py-4"},w={key:0},_={class:"text-center px-3 py-4"},V={key:0},k={class:"text-center px-3 py-4"},x={key:0},N={class:"text-center px-3 py-4"},E={key:0},B={class:""},S=["onClick"],C=Object(n["createElementVNode"])("td",null,null,-1);var I={__name:"TableJuveniles",props:{tableBody:{type:Array,required:!0}},emits:["sort-by-date"],setup(e){return(e,t)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("table",s,[Object(n["createElementVNode"])("thead",null,[Object(n["createElementVNode"])("tr",l,[o,u,Object(n["createElementVNode"])("th",{class:"py-4 pl-3 cursor-pointer",onClick:t[0]||(t[0]=t=>e.$emit("sort-by-date"))}," Tug’ilgan sanasi "),d,p,b,v,g,j])]),Object(n["createElementVNode"])("tbody",null,[(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(e.$props.tableBody,(t,a)=>{var i,r;return Object(n["openBlock"])(),Object(n["createElementBlock"])("tr",{key:t.id,class:"text-gray-800 odd:bg-white even:bg-grayPrimary !hover:bg-gray-200"},[Object(n["createElementVNode"])("td",y,[Object(n["createElementVNode"])("div",m,Object(n["toDisplayString"])(a+1),1)]),Object(n["createElementVNode"])("td",f,[Object(n["createElementVNode"])("div",h,Object(n["toDisplayString"])(`${t.first_name}  ${t.last_name} ${t.father_name}`),1)]),Object(n["createElementVNode"])("td",O,[t.birth_date?(Object(n["openBlock"])(),Object(n["createElementBlock"])("span",w,Object(n["toDisplayString"])(t.birth_date),1)):Object(n["createCommentVNode"])("",!0)]),Object(n["createElementVNode"])("td",_,[t.time_arrival_center?(Object(n["openBlock"])(),Object(n["createElementBlock"])("span",V,Object(n["toDisplayString"])(t.time_arrival_center),1)):Object(n["createCommentVNode"])("",!0)]),Object(n["createElementVNode"])("td",k,[null!==t&&void 0!==t&&null!==(i=t.status)&&void 0!==i&&i.text?(Object(n["openBlock"])(),Object(n["createElementBlock"])("span",x,Object(n["toDisplayString"])(null===t||void 0===t||null===(r=t.status)||void 0===r?void 0:r.text),1)):Object(n["createCommentVNode"])("",!0)]),Object(n["createElementVNode"])("td",N,[t.time_departure_center?(Object(n["openBlock"])(),Object(n["createElementBlock"])("span",E,Object(n["toDisplayString"])(t.time_departure_center),1)):Object(n["createCommentVNode"])("",!0)]),Object(n["createElementVNode"])("td",B,[Object(n["createElementVNode"])("button",{class:"mx-auto px-4 flex gap-4 py-2 text-primary hover:text-white hover:bg-primary rounded-md",onClick:a=>e.$router.push("/teenager/"+t.id)},[Object(n["createTextVNode"])(" Ko'rish "),Object(n["createVNode"])(Object(n["unref"])(c["a"]),{icon:"mdi:eye",width:"20",height:"20"})],8,S)]),C])}),128))])]))}};const z=I;var T=z,D=a("7c27"),P=a("1a02"),L=a("b4b5"),R=a("2eed"),J=a("4b59");function $(){const e=Object(n["ref"])([]),t=async()=>{const{data:t}=await J["a"].fetchJuvenileStatuses();e.value=t};return Object(n["onMounted"])(async()=>{await t()}),{juvenileStatuses:e}}var M=a("a5a1"),q=a("8b9c"),A=a("2e00"),U=a("89ed"),F=a("e19e");const H={class:"bg-white rounded-md p-3"},K={class:"grid grid-cols-2 md:grid-cols-4 gap-4"},G={class:"form_wrapper my-3"},X={class:"form_wrapper my-3"},W={class:"form_wrapper my-3"},Q={class:"flex items-center gap-2 my-3"};var Y={__name:"Juveniles",setup(e){const{fetchJuvenileReportsList:t}=U["a"],{regionsList:a}=Object(L["a"])(),{schoolTypes:i}=Object(P["a"])(),{juvenileStatuses:s}=$(),{currentPage:l,pageSize:o,allPagesCount:u,pageSizeOptions:d}=Object(R["a"])([10,15,20]),p=Object(n["ref"])([]),b=Object(n["ref"])(!0),{alertThisError:v}=Object(F["a"])(),g=Object(n["ref"])("ASC"),j=Object(n["ref"])(""),y=Object(n["ref"])(""),m=Object(n["ref"])(""),f=Object(n["ref"])(""),h=async e=>{try{b.value=!0;const a=await t({...e});p.value=null===a||void 0===a?void 0:a.results,u.value=null===a||void 0===a?void 0:a.num_pages,l.value=null===a||void 0===a?void 0:a.current,b.value=!1}catch(a){v(a)}};function O(){"ASC"===g.value?(g.value="DESC",p.value.sort((function(e,t){return new Date(t.birth_date)-new Date(e.birth_date)}))):(g.value="ASC",p.value.sort((function(e,t){return new Date(e.birth_date)-new Date(t.birth_date)})))}return Object(n["watch"])([m,j,y,o,l,f],async([e,t,a,n,i,r])=>{await h({full_name:e,school_type:t,address_region:a,page_size:n,page:i,status:r})},{immediate:!0}),(e,t)=>{const v=Object(n["resolveDirective"])("validate-cyrillic");return Object(n["openBlock"])(),Object(n["createElementBlock"])("section",H,[Object(n["createVNode"])(Object(n["unref"])(A["a"]),null,{default:Object(n["withCtx"])(()=>[Object(n["createTextVNode"])(" Bolalar ro'yxati ")]),_:1}),Object(n["createVNode"])(Object(n["unref"])(D["a"]),{"current-page":Object(n["unref"])(l),"onUpdate:current-page":t[6]||(t[6]=e=>Object(n["isRef"])(l)?l.value=e:null),"page-size":Object(n["unref"])(o),"onUpdate:page-size":t[7]||(t[7]=e=>Object(n["isRef"])(o)?o.value=e:null),"page-size-options":Object(n["unref"])(d),"all-pages-count":Object(n["unref"])(u),onTableOptionsChanged:h},Object(n["createSlots"])({"filter-additional-content":Object(n["withCtx"])(()=>[Object(n["createElementVNode"])("div",K,[Object(n["createElementVNode"])("div",G,[Object(n["withDirectives"])(Object(n["createElementVNode"])("input",{id:"search","onUpdate:modelValue":t[0]||(t[0]=e=>m.value=e),placeholder:"F.I.SH bo'yicha qidirish",class:"base_input",name:"search",type:"text"},null,512),[[v],[n["vModelText"],m.value]])]),Object(n["createElementVNode"])("div",X,[Object(n["createVNode"])(Object(n["unref"])(M["a"]),{id:"address_region",modelValue:y.value,"onUpdate:modelValue":t[1]||(t[1]=e=>y.value=e),options:Object(n["unref"])(q["a"])(Object(n["unref"])(a),"name","id","Barcha viloyatlar bo'yicha"),"show-by":"name","track-by":"id",placeholder:"Viloyat bo'yicha"},null,8,["modelValue","options"])]),Object(n["createElementVNode"])("div",W,[Object(n["createVNode"])(Object(n["unref"])(M["a"]),{id:"school_type",modelValue:j.value,"onUpdate:modelValue":t[2]||(t[2]=e=>j.value=e),options:Object(n["unref"])(q["a"])(Object(n["unref"])(i),"text","id","Barcha muassasa turlari bo'yicha"),"show-by":"text","track-by":"id",placeholder:"Ta`lim muassasa bo'yicha"},null,8,["modelValue","options"])]),Object(n["createElementVNode"])("div",Q,[Object(n["createVNode"])(Object(n["unref"])(M["a"]),{id:"status",modelValue:f.value,"onUpdate:modelValue":t[3]||(t[3]=e=>f.value=e),options:Object(n["unref"])(q["a"])(Object(n["unref"])(s),"text","id","Barcha holatlar bo'yicha "),"show-by":"text","track-by":"id",placeholder:"Holatlar bo'yicha"},null,8,["modelValue","options"]),Object(n["createElementVNode"])("button",{onClick:t[4]||(t[4]=t=>e.$router.go()),class:"base_input !w-auto"},[Object(n["createVNode"])(Object(n["unref"])(c["a"]),{icon:"mdi:close"})])])])]),_:2},[b.value?{name:"loading",fn:Object(n["withCtx"])(()=>[Object(n["createVNode"])(Object(n["unref"])(r.a),{active:b.value,"onUpdate:active":t[5]||(t[5]=e=>b.value=e),"can-cancel":!1,"is-full-page":!1,color:"#4785FE",loader:"dots"},null,8,["active"])]),key:"0"}:{name:"table-content",fn:Object(n["withCtx"])(()=>[Object(n["createVNode"])(Object(n["unref"])(T),{"table-body":p.value,onSortByDate:O},null,8,["table-body"])]),key:"1"}]),1032,["current-page","page-size","page-size-options","all-pages-count"])])}}};const Z=Y;t["default"]=Z},"2e00":function(e,t,a){"use strict";var n=a("7a23");const i={class:"text-2xl my-4"};function r(e,t,a,r,c,s){return Object(n["openBlock"])(),Object(n["createElementBlock"])("h1",i,[Object(n["renderSlot"])(e.$slots,"default")])}var c={name:"PageTitle"},s=a("d959"),l=a.n(s);const o=l()(c,[["render",r]]);t["a"]=o},"2eed":function(e,t,a){"use strict";a.d(t,"a",(function(){return r}));a("14d9");var n=a("7a23"),i=a("6605");function r(e=[10,15,20]){const t=Object(i["d"])(),a=Object(i["c"])(),r=Object(n["ref"])(0),c=Object(n["ref"])(1),s=Object(n["ref"])(e),l=Object(n["ref"])(10);function o(e){l.value=e}function u(e){c.value=e}function d(){const{page:e,page_size:t}=null===a||void 0===a?void 0:a.query;e&&(c.value=+e),t&&(l.value=+t)}return d(),Object(n["watch"])(()=>l.value,e=>{e&&t.push({path:a.path,query:{...null===a||void 0===a?void 0:a.query,page_size:e}})}),Object(n["watch"])(()=>c.value,e=>{e&&t.push({path:a.path,query:{...null===a||void 0===a?void 0:a.query,page:e}})}),{allPagesCount:r,currentPage:c,pageSizeOptions:s,pageSize:l,setPageSize:o,setCurrentPage:u}}},"4b59":function(e,t,a){"use strict";var n=a("451b");const i={async fetchArrivedReasons(){return n["a"].get("api/juvenile/juveniles/arrived_reasons/")},async fetchMonitoringTypes(){return n["a"].get("api/juvenile/juveniles/monitoring_status/")},async fetchBasisDistributions(){return await n["a"].get("/api/juvenile/juveniles/basis_distributions/")},async fetchBringingReasonList(){return await n["a"].get("api/info/reason_bringing_child")},async fetchCharactersList(){return await n["a"].get("api/juvenile/juveniles/characters/")},async fetchConvictedTypesList(){return await n["a"].get("/api/juvenile/juveniles/convicted_lists/")},async fetchCountComeBack(){return await n["a"].get("api/juvenile/juveniles/get_came_back_center/")},async fetchCountries(){return await n["a"].get("api/info/countries/")},async fetchDeterminedLocations(){return await n["a"].get("/api/juvenile/juveniles/determined_locations/")},async fetchDistributionTypes(){return await n["a"].get("/api/juvenile/juveniles/distribution_types")},async fetchEducationTypes(){return await n["a"].get("/api/juvenile/juveniles/employment_education_types/")},async fetchGuardianshipTypes(){return await n["a"].get("/api/juvenile/juveniles/type_guardianships/")},async fetchHaveBeenInItmTypes(){return await n["a"].get("/api/juvenile/juveniles/have_been_in_itm_reasons/")},async fetchHaveBeenInRotmTypes(){return await n["a"].get("/api/juvenile/juveniles/have_been_in_rotm_reasons/")},async fetchHealthCareFacility(){return await n["a"].get("/api/juvenile/juveniles/type_healthcare_facility/")},async fetchInspectorTypesList(){return await n["a"].get("/api/juvenile/juveniles/inspector_types")},async fetchITMDirections(){return await n["a"].get("/api/juvenile/juveniles/itm_directions/")},async fetchJuvenileStatuses(){return await n["a"].get("api/juvenile/juveniles/juvenile_statuses")},async fetchLevelsKindship(){return await n["a"].get("api/juvenile/juveniles/level_kindships/")},async fetchMaritalStatuses(){return await n["a"].get("/api/juvenile/juveniles/marital_statuses/")},async fetchMarkazs(){return await(await n["a"].get("/api/info/markazs/"))},async fetchMasteryLevelList(){return await n["a"].get("api/juvenile/juveniles/mastery/")},async fetchMedicalListTypes(){return await n["a"].get("/api/info/medical_list/")},async fetchParentTypesList(){return await n["a"].get("/api/juvenile/juveniles/parent_types/")},async fetchPassportTypes(){return await n["a"].get("/api/juvenile/juveniles/passport_types/")},async fetchPositions(){return await n["a"].get("/auth/groups/")},async fetchROTMDirections(){return await n["a"].get("/api/juvenile/juveniles/rotm_types/")},async fetchSchoolTypes(){return await n["a"].get("/api/juvenile/juveniles/school_types")},async fetchSchoolsListByTypeAndRegionId(e,t){return await n["a"].get("/api/info/schools/ByTypeIdAndDistrictId/",{params:{school_type:e,district:t}})},async fetchKindergartens(e){return await n["a"].get("/api/info/kindergartens/ByDistrictId/",{params:{district:e.target.value}})},async fetchSchoolList(e){return await n["a"].get("/api/info/schools/ByDistrictId/",{params:{district:e.target.value}})},async fetchUniversitiesListByRegionId(e){return await n["a"].get("/api/info/universities/ByRegionId/",{params:{region:e.target.value}})},async fetchCollegesListByRegionId(e){return await n["a"].get("api/info/colleges/ByRegionId/",{params:{region:e.target.value}})},async fetchSpecialEducationListByRegionId(e){return await n["a"].get("/api/info/special_educations/ByRegionId/",{params:{region:e.target.value}})},async fetchVocationalSchoolsListByRegionId(e){return await n["a"].get("/api/info/vocational_schools/ByRegionId/",{params:{region:e.target.value}})},async fetchLitseysListByRegionId(e){return await n["a"].get("/api/info/litsey/ByRegionId/",{params:{region:e.target.value}})},async fetchTexnikumsListByRegionId(e){return await n["a"].get("/api/info/texnikums/ByRegionId/",{params:{region:e.target.value}})},async fetchSubBringingReasonList(e){return await n["a"].get("/api/info/subreasonbringing_child_by_parent/",{params:{parent:e.target.value}})},async fetchWhomGivenList(){return await n["a"].get("/api/juvenile/juveniles/foreign_to_whom_given/")},async fetchRegion(e){return await n["a"].get("/api/info/markaz_tumans/",{params:{region_id:e}})}};t["a"]=i},"7c27":function(e,t,a){"use strict";var n=a("7a23");const i={class:"flex bg-white items-center justify-between font-light text-sm xl:text-md py-3 px-4"},r={class:"flex items-center"},c={class:"relative inline-block text-left"},s=Object(n["createElementVNode"])("svg",{class:"-mr-1 ml-2 h-5 w-5",xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 20 20",fill:"currentColor","aria-hidden":"true"},[Object(n["createElementVNode"])("path",{"fill-rule":"evenodd",d:"M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z","clip-rule":"evenodd"})],-1),l={key:0,class:"origin-top-right absolute z-30 left-0 mt-2 w-20 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none",role:"menu","aria-orientation":"vertical","aria-labelledby":"menu-button",tabindex:"-1"},o={class:"py-1",role:"none"},u=["onClick"],d=Object(n["createElementVNode"])("span",{class:"ml-4"},"Ko‘rsatish soni",-1),p={class:"flex items-center"},b={class:"mx-2 px-2 py-1 rounded border border-blue-500 ring-1 ring-indigo-600 ring-opacity-70"},v={class:"mx-2"},g=["disabled"],j=Object(n["createElementVNode"])("svg",{xmlns:"http://www.w3.org/2000/svg",class:"h-6 w-6",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(n["createElementVNode"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M15 19l-7-7 7-7"})],-1),y=[j],m=["disabled"],f=Object(n["createElementVNode"])("svg",{xmlns:"http://www.w3.org/2000/svg",class:"h-6 w-6",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(n["createElementVNode"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M9 5l7 7-7 7"})],-1),h=[f];var O={__name:"Pagination",props:{allPagesCount:{required:!0,type:Number},pageSize:{required:!0,type:Number},currentPage:{required:!0,type:Number},pageSizeOptions:{type:Array,required:!0}},emits:["page-size-changed","pagination-btn-clicked"],setup(e,{emit:t}){const a=e,j=Object(n["ref"])(!1),f=Object(n["computed"])(()=>a.currentPage===a.allPagesCount||0===a.allPagesCount),O=Object(n["computed"])(()=>1===a.currentPage||0===a.allPagesCount);function w(){t("pagination-btn-clicked","PREV")}function _(){t("pagination-btn-clicked","NEXT")}function V(e){t("page-size-changed",e),j.value=!1}return(t,a)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",i,[Object(n["createElementVNode"])("div",r,[Object(n["createElementVNode"])("div",c,[Object(n["createElementVNode"])("div",null,[Object(n["createElementVNode"])("button",{id:"menu-button",type:"button",class:"inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500","aria-expanded":"true","aria-haspopup":"true",onClick:a[0]||(a[0]=e=>j.value=!j.value)},[Object(n["createTextVNode"])(Object(n["toDisplayString"])(e.pageSize)+" ",1),s])]),j.value?(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",l,[Object(n["createElementVNode"])("div",o,[(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(e.pageSizeOptions,e=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("a",{id:"menu-item-0",key:e,class:"text-gray-700 block px-4 py-2 text-sm active:bg-gray-100 active:text-gray-900",role:"menuitem",tabindex:"-1",onClick:t=>V(e)},Object(n["toDisplayString"])(e),9,u))),128))])])):Object(n["createCommentVNode"])("",!0)]),d]),Object(n["createElementVNode"])("div",p,[Object(n["createElementVNode"])("p",null,[Object(n["createElementVNode"])("span",b,Object(n["toDisplayString"])(e.currentPage),1),Object(n["createTextVNode"])(" dan "),Object(n["createElementVNode"])("span",v,Object(n["toDisplayString"])(e.allPagesCount),1)]),Object(n["createElementVNode"])("button",{class:Object(n["normalizeClass"])(["px-1 py-1 mr-3 rounded bg-gray-200",{"opacity-40 cursor-not-allowed hover:bg-gray-200 hover:text-black":Object(n["unref"])(O),"hover:bg-indigo-600 hover:text-white":!Object(n["unref"])(O)}]),disabled:Object(n["unref"])(O),onClick:w},y,10,g),Object(n["createElementVNode"])("button",{class:Object(n["normalizeClass"])(["px-1 py-1 rounded bg-gray-200",{"opacity-40 cursor-not-allowed hover:bg-gray-200 hover:text-black":Object(n["unref"])(f),"hover:bg-indigo-600 hover:text-white":!Object(n["unref"])(f)}]),disabled:Object(n["unref"])(f),onClick:_},h,10,m)])]))}};const w=O;var _=w;const V={class:"bg-white p-3"},k={class:"bg-white px-3 flex justify-between items-center"};var x={__name:"TableView",props:{allPagesCount:{type:Number,default:1},currentPage:{type:Number,default:1},pageSize:{type:Number,required:!0,default:1},showStatusTab:{type:Boolean,default:!0},pageSizeOptions:{type:Array,default:function(){return[10,15,20,50]}}},emits:["table-options-changed","update:current-page","update:page-size"],setup(e,{emit:t}){const a=e;async function i(e){"PREV"===e&&t("update:current-page",a.currentPage-1),"NEXT"===e&&t("update:current-page",a.currentPage+1)}async function r(e){t("update:page-size",e)}return(t,a)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",V,[Object(n["createElementVNode"])("div",k,[Object(n["renderSlot"])(t.$slots,"filter-additional-content")]),Object(n["renderSlot"])(t.$slots,"loading"),Object(n["renderSlot"])(t.$slots,"table-content"),Object(n["createVNode"])(Object(n["unref"])(_),{"page-size-options":e.pageSizeOptions,"page-size":e.pageSize,"all-pages-count":e.allPagesCount,"current-page":e.currentPage,onPaginationBtnClicked:i,onPageSizeChanged:r},null,8,["page-size-options","page-size","all-pages-count","current-page"])]))}};const N=x;t["a"]=N},"89ed":function(e,t,a){"use strict";var n=a("451b");const i={async fetchJuvenileById(e){const{data:t}=await n["a"].get(`/api/juvenile/juveniles/${e}/`);return t},async fetchJuvenileInfoDetailById(e){const{data:t}=await n["a"].get(`/api/juvenile/juveniles/${e}/juvenile_info_detail/`);return t},async fetchJuvenilesList(e={}){return(await n["a"].get("/api/juvenile/juveniles/",{params:e})).data},async fetchJuvenileReportsList(e={}){return(await n["a"].get("/api/juvenile/reports/",{params:{...e}})).data},async fetchJuvenileReportById(e){const{data:t}=await n["a"].get(`/api/juvenile/is_filled/${e}/`);return t},async fetchJuvenileReportsInfoById(e){const{data:t}=await n["a"].get("/api/juvenile/reports/"+e);return t},async fetchAcceptedJuvenilesInfo(e){const{data:t}=await n["a"].get(`/api/juvenile/accepted_for_edit/${e}/`);return t},async acceptJuvenileToCenter(e,t){return await n["a"].post("/api/juvenile/juveniles/accept_juvenile/",t,{params:{juvenile_id:e}})},async createAvailableJuvenile(e){return await n["a"].post("/api/juvenile/juveniles/create_available_juvenile/?juvenile_id="+e)},async updateJuvenile(e,t){return await n["a"].put("/api/juvenile/juveniles/"+t,e)},async createJuvenilePersonalInfo(e){return await n["a"].post("/api/juvenile/juveniles/",e)},async createJuvenileAddressInfo(e,t){return await n["a"].post(`/api/juvenile/juveniles/${e}/juvenile_addressinfo_create_or_update/`,t)},async createJuvenileEducationInfo(e,t){return await n["a"].post(`/api/juvenile/juveniles/${e}/juvenile_educationinfo_create_or_update/`,t)},async getDeterminedJuvenilesList(e){const t=(await n["a"].get("/api/juvenile/juveniles/incomplete_juveniles/",{params:e})).data,a=t.results.map(e=>({birth_date:e.personal_info.birth_date,father_name:e.personal_info.father_name,first_name:e.personal_info.first_name,last_name:e.personal_info.last_name,...e}));return{...t,results:a}},async getNotDefinedJuvenilesList(e){return(await n["a"].get("/api/juvenile/juveniles/unidentified_juveniles",{params:e})).data},async delete_incomplete_juvenile(e){return await n["a"].delete(`/api/juvenile/juveniles/${e}/delete_incomplete_juvenile/`)},async delete_unidentified_juvenile(e){return await n["a"].delete(`/api/juvenile/juveniles/${e}/delete_unidentified_juvenile/`)}};t["a"]=i},"8b9c":function(e,t,a){"use strict";function n(e,t,a,n){return[...e,{[t]:n,[a]:""}]}a.d(t,"a",(function(){return n}))},b4b5:function(e,t,a){"use strict";a.d(t,"a",(function(){return r}));var n=a("7a23"),i=a("ba1a");function r(e){const t=Object(n["ref"])([]),a=async()=>{const{data:e}=await i["a"].fetchRegions();t.value=e};return Object(n["onMounted"])(async()=>{await a()}),{regionsList:t}}},b7a4:function(e,t,a){"use strict";a.d(t,"a",(function(){return i}));var n=a("0180");function i(){const e=Object(n["b"])();function t(t,a=["success","error","danger","info"][0]){e(t,{type:a})}return{alertIt:t}}},ba1a:function(e,t,a){"use strict";var n=a("451b");const i={async fetchRegions(){try{return await n["a"].get("api/info/regions/")}catch(e){console.log(e)}},async fetchDistrictsByRegionId(e){try{return await n["a"].get("/api/info/districts/ByRegionId/",{params:{region:e.target.value}})}catch(t){console.log(t)}},async fetchMahallaByDistrictId(e){try{return await n["a"].get("api/info/mahalla/ByDistrictId/",{params:{district:e.target.value}})}catch(t){console.log(t)}}};t["a"]=i},e19e:function(e,t,a){"use strict";a.d(t,"a",(function(){return i}));var n=a("b7a4");function i(){const{alertIt:e}=Object(n["a"])(),t=t=>{var a,n,i,r,c,s,l,o,u,d,p;if(console.log({error:t},"UseErrorAlert"),"string"===typeof(null===t||void 0===t||null===(a=t.response)||void 0===a||null===(n=a.data)||void 0===n?void 0:n.message))e(null===t||void 0===t||null===(d=t.response)||void 0===d||null===(p=d.data)||void 0===p?void 0:p.message,"error");else if(null!==t&&void 0!==t&&null!==(i=t.response)&&void 0!==i&&i.data&&"string"!==typeof(null===t||void 0===t||null===(r=t.response)||void 0===r?void 0:r.data)&&null!==t&&void 0!==t&&null!==(c=t.response)&&void 0!==c&&null!==(s=c.data)&&void 0!==s&&s.messages)Object.values(t.response.data.messages).map(t=>{null!==t&&void 0!==t&&t.message&&e(t.message,"error")});else if(Array.isArray(null===t||void 0===t||null===(l=t.response)||void 0===l?void 0:l.data)){var b;null===t||void 0===t||null===(b=t.response)||void 0===b||b.data.map(t=>{e(t,"error")})}else null!==t&&void 0!==t&&null!==(o=t.response)&&void 0!==o&&o.data&&400===(null===t||void 0===t||null===(u=t.response)||void 0===u?void 0:u.status)?Object.values(t.response.data).map(t=>{"string"==typeof t?e(t,"error"):t.map(t=>e(t,"error"))}):e("Server bilan bog'liq xatolik yuz berdi.","error")};return{alertThisError:t}}}}]);
//# sourceMappingURL=chunk-6b4dd38f.5580170c.js.map