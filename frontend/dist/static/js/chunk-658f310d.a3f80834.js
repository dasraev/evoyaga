(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-658f310d"],{"3ee4":function(e,t,a){"use strict";a.r(t);var l=a("7a23"),n=a("9062"),o=a.n(n),c=(a("e40d"),a("6605")),r=a("451b"),s=a("5779"),i=a("90a7"),p=a("e19e");const d={key:1,class:"w-full bg-white rounded-md"},b={class:"w-full mx-auto lg:w-[65%] xl:w-[55%] px-2 py-12"},u=["src"],m={class:""},j={class:"info_wrapper"},v=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"To'lliq ismi:",-1),O={class:"info_wrapper_text"},_={class:"info_wrapper"},f=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Tug’ilgan sanasi:",-1),w={class:"info_wrapper_text"},E={class:"info_wrapper"},V=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Tug’ilgan sanasi:",-1),g={class:"info_wrapper_text"},N={key:0,class:"info_wrapper"},k=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Passport seriyasi:",-1),y={class:"info_wrapper_text"},x={key:1,class:"info_wrapper"},h=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"JSHSHIR",-1),B={class:"info_wrapper_text"},S={class:"info_wrapper"},D=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Taqsimot turi :",-1),T={class:"info_wrapper_text"},C={class:"info_wrapper"},M=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Taqsimot asos fayli",-1),q={class:"info_wrapper_text flex items-center gap-4"},I={class:""},G=["href","download"],A={class:"info_wrapper"},H=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Taqsimot asosi :",-1),J={class:"info_wrapper_text"},$={key:2,class:"info_wrapper"},P=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Qarindoshlik darajasi :",-1),R={class:"info_wrapper_text"},U={key:3,class:"info_wrapper"},W=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"Vasiylik turi :",-1),z={class:"info_wrapper_text"},F={key:4,class:"info_wrapper"},Q=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"},"RO’TM turi :",-1),Y={class:"info_wrapper_text"},K={key:5},L={class:"info_wrapper"},X=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"}," ITM yo’nalishi :",-1),Z={class:"info_wrapper_text"},ee={class:"info_wrapper"},te=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"}," ITM joylashgan viloyati :",-1),ae={class:"info_wrapper_text"},le={class:"info_wrapper"},ne=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"}," ITM joylashgan tuman :",-1),oe={class:"info_wrapper_text"},ce={class:"info_wrapper"},re=Object(l["createElementVNode"])("span",{class:"info_wrapper_label"}," ITM nomi :",-1),se={class:"info_wrapper_text"};var ie={__name:"AllocatedJuvenileInfo",setup(e){const t=Object(c["c"])(),a=Object(l["ref"])(null),n=Object(l["ref"])(!0),{alertThisError:ie}=Object(p["a"])();Object(l["onMounted"])(async()=>{await pe()});const pe=async()=>{try{n.value=!0,a.value=(await r["a"].get(`/api/juvenile/juveniles/${t.params.id}/is_out_detail/`)).data,n.value=!1}catch(e){n.value=!1,ie(e)}};return(e,t)=>{var c,r,p,ie,pe,de,be,ue;return n.value?(Object(l["openBlock"])(),Object(l["createBlock"])(Object(l["unref"])(o.a),{key:0,active:n.value,"onUpdate:active":t[0]||(t[0]=e=>n.value=e),"can-cancel":!1,"is-full-page":!0,color:"#4785FE",loader:"dots"},null,8,["active"])):(Object(l["openBlock"])(),Object(l["createElementBlock"])("main",d,[Object(l["createVNode"])(Object(l["unref"])(i["a"]),null,{default:Object(l["withCtx"])(()=>[Object(l["createTextVNode"])(" Taqsimlangan bola haqida ma'lumot ")]),_:1}),Object(l["createElementVNode"])("div",b,[Object(l["createElementVNode"])("img",{src:a.value.photo||"https://images.unsplash.com/photo-1608734265656-f035d3e7bcbf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",class:"w-[150px] h-[150px] object-contain object-top rounded-full mx-auto mb-3"},null,8,u),Object(l["createElementVNode"])("div",m,[Object(l["createElementVNode"])("div",j,[v,Object(l["createElementVNode"])("p",O,Object(l["toDisplayString"])(a.value.second_name)+" "+Object(l["toDisplayString"])(a.value.first_name)+" "+Object(l["toDisplayString"])(a.value.father_name),1)]),Object(l["createElementVNode"])("div",_,[f,Object(l["createElementVNode"])("p",w,Object(l["toDisplayString"])(a.value.birth_date),1)]),Object(l["createElementVNode"])("div",E,[V,Object(l["createElementVNode"])("p",g,Object(l["toDisplayString"])(a.value.birth_date),1)]),a.value.passport_seria?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",N,[k,Object(l["createElementVNode"])("p",y,Object(l["toDisplayString"])(a.value.passport_seria),1)])):Object(l["createCommentVNode"])("",!0),a.value.pinfl?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",x,[h,Object(l["createElementVNode"])("p",B,Object(l["toDisplayString"])(a.value.pinfl),1)])):Object(l["createCommentVNode"])("",!0),Object(l["createElementVNode"])("div",S,[D,Object(l["createElementVNode"])("p",T,Object(l["toDisplayString"])(null===(c=a.value.distribution_type)||void 0===c?void 0:c.text),1)]),Object(l["createElementVNode"])("div",C,[M,Object(l["createElementVNode"])("div",q,[Object(l["createElementVNode"])("p",I,Object(l["toDisplayString"])(a.value.basis_sending_file.name),1),a.value.basis_sending_file?(Object(l["openBlock"])(),Object(l["createElementBlock"])("a",{key:0,target:"_blank",href:a.value.basis_sending_file.path,download:a.value.basis_sending_file.path,class:"flex flex-col bg-gray-100 rounded-md p-1 items-center justify-center"},[Object(l["createVNode"])(Object(l["unref"])(s["a"]),{icon:"mdi:file",width:"32"})],8,G)):(Object(l["openBlock"])(),Object(l["createBlock"])(Object(l["unref"])(s["a"]),{key:1,icon:"mdi:minus-circle",width:"32",class:""}))])]),Object(l["createElementVNode"])("div",A,[H,Object(l["createElementVNode"])("p",J,Object(l["toDisplayString"])(null===(r=a.value.basis_distribution)||void 0===r?void 0:r.text),1)]),a.value.level_kinkdship?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",$,[P,Object(l["createElementVNode"])("p",R,Object(l["toDisplayString"])(null===(p=a.value.level_kinkdship)||void 0===p?void 0:p.text),1)])):Object(l["createCommentVNode"])("",!0),a.value.type_guardianship?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",U,[W,Object(l["createElementVNode"])("p",z,Object(l["toDisplayString"])(null===(ie=a.value.type_guardianship)||void 0===ie?void 0:ie.text),1)])):Object(l["createCommentVNode"])("",!0),a.value.rotm_type?(Object(l["openBlock"])(),Object(l["createElementBlock"])("div",F,[Q,Object(l["createElementVNode"])("p",Y,Object(l["toDisplayString"])(null===(pe=a.value.rotm_type)||void 0===pe?void 0:pe.text),1)])):Object(l["createCommentVNode"])("",!0),a.value.itm_direction?(Object(l["openBlock"])(),Object(l["createElementBlock"])("section",K,[Object(l["createElementVNode"])("div",L,[X,Object(l["createElementVNode"])("p",Z,Object(l["toDisplayString"])(null===(de=a.value.itm_direction)||void 0===de?void 0:de.text),1)]),Object(l["createElementVNode"])("div",ee,[te,Object(l["createElementVNode"])("p",ae,Object(l["toDisplayString"])(null===(be=a.value.itm_region)||void 0===be?void 0:be.name),1)]),Object(l["createElementVNode"])("div",le,[ne,Object(l["createElementVNode"])("p",oe,Object(l["toDisplayString"])(null===(ue=a.value.itm_district)||void 0===ue?void 0:ue.name),1)]),Object(l["createElementVNode"])("div",ce,[re,Object(l["createElementVNode"])("p",se,Object(l["toDisplayString"])(a.value.itm_name),1)])])):Object(l["createCommentVNode"])("",!0)])])]))}}};const pe=ie;t["default"]=pe},"90a7":function(e,t,a){"use strict";var l=a("7a23");const n={class:"flex items-center gap-5"};function o(e,t,a,o,c,r){const s=Object(l["resolveComponent"])("GoBackBtn");return Object(l["openBlock"])(),Object(l["createElementBlock"])("div",n,[Object(l["createVNode"])(s),Object(l["createElementVNode"])("h1",null,[Object(l["renderSlot"])(e.$slots,"default")])])}const c=Object(l["createElementVNode"])("svg",{xmlns:"http://www.w3.org/2000/svg",class:"h-6 w-6 text-blue-400",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(l["createElementVNode"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M11 17l-5-5m0 0l5-5m-5 5h12"})],-1),r=[c];function s(e,t,a,n,o,c){return Object(l["openBlock"])(),Object(l["createElementBlock"])("button",{class:"clickEffectBtn px-4 py-2",onClick:t[0]||(t[0]=t=>e.$router.back())},r)}var i={name:"GoBackBtn"},p=a("d959"),d=a.n(p);const b=d()(i,[["render",s]]);var u=b,m={name:"PageTitleWithGoBackButton",components:{GoBackBtn:u}};const j=d()(m,[["render",o]]);t["a"]=j},b7a4:function(e,t,a){"use strict";a.d(t,"a",(function(){return n}));var l=a("0180");function n(){const e=Object(l["b"])();function t(t,a=["success","error","danger","info"][0]){e(t,{type:a})}return{alertIt:t}}},e19e:function(e,t,a){"use strict";a.d(t,"a",(function(){return n}));var l=a("b7a4");function n(){const{alertIt:e}=Object(l["a"])(),t=t=>{var a,l,n,o,c,r,s,i,p,d,b;if(console.log({error:t},"UseErrorAlert"),"string"===typeof(null===t||void 0===t||null===(a=t.response)||void 0===a||null===(l=a.data)||void 0===l?void 0:l.message))e(null===t||void 0===t||null===(d=t.response)||void 0===d||null===(b=d.data)||void 0===b?void 0:b.message,"error");else if(null!==t&&void 0!==t&&null!==(n=t.response)&&void 0!==n&&n.data&&"string"!==typeof(null===t||void 0===t||null===(o=t.response)||void 0===o?void 0:o.data)&&null!==t&&void 0!==t&&null!==(c=t.response)&&void 0!==c&&null!==(r=c.data)&&void 0!==r&&r.messages)Object.values(t.response.data.messages).map(t=>{null!==t&&void 0!==t&&t.message&&e(t.message,"error")});else if(Array.isArray(null===t||void 0===t||null===(s=t.response)||void 0===s?void 0:s.data)){var u;null===t||void 0===t||null===(u=t.response)||void 0===u||u.data.map(t=>{e(t,"error")})}else null!==t&&void 0!==t&&null!==(i=t.response)&&void 0!==i&&i.data&&400===(null===t||void 0===t||null===(p=t.response)||void 0===p?void 0:p.status)?Object.values(t.response.data).map(t=>{"string"==typeof t?e(t,"error"):t.map(t=>e(t,"error"))}):e("Server bilan bog'liq xatolik yuz berdi.","error")};return{alertThisError:t}}}}]);
//# sourceMappingURL=chunk-658f310d.a3f80834.js.map