(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0c8dfa"],{5779:function(t,e,n){"use strict";n.d(e,"a",(function(){return ne}));var o=n("7a23");const r=/^[a-z0-9]+(-[a-z0-9]+)*$/,i=Object.freeze({left:0,top:0,width:16,height:16,rotate:0,vFlip:!1,hFlip:!1});function c(t){return{...i,...t}}const s=(t,e,n,o="")=>{const r=t.split(":");if("@"===t.slice(0,1)){if(r.length<2||r.length>3)return null;o=r.shift().slice(1)}if(r.length>3||!r.length)return null;if(r.length>1){const t=r.pop(),n=r.pop(),i={provider:r.length>0?r[0]:o,prefix:n,name:t};return e&&!a(i)?null:i}const i=r[0],c=i.split("-");if(c.length>1){const t={provider:o,prefix:c.shift(),name:c.join("-")};return e&&!a(t)?null:t}if(n&&""===o){const t={provider:o,prefix:"",name:i};return e&&!a(t,n)?null:t}return null},a=(t,e)=>!!t&&!(""!==t.provider&&!t.provider.match(r)||!(e&&""===t.prefix||t.prefix.match(r))||!t.name.match(r));function l(t,e){const n={...t};for(const o in i){const t=o;if(void 0!==e[t]){const o=e[t];if(void 0===n[t]){n[t]=o;continue}switch(t){case"rotate":n[t]=(n[t]+o)%4;break;case"hFlip":case"vFlip":n[t]=o!==n[t];break;default:n[t]=o}}}return n}function u(t,e,n=!1){function o(e,n){if(void 0!==t.icons[e])return Object.assign({},t.icons[e]);if(n>5)return null;const r=t.aliases;if(r&&void 0!==r[e]){const t=r[e],i=o(t.parent,n+1);return i?l(i,t):i}const i=t.chars;return!n&&i&&void 0!==i[e]?o(i[e],n+1):null}const r=o(e,0);if(r)for(const c in i)void 0===r[c]&&void 0!==t[c]&&(r[c]=t[c]);return r&&n?c(r):r}function f(t){for(const e in i)if(void 0!==t[e])return!0;return!1}function d(t,e,n){n=n||{};const o=[];if("object"!==typeof t||"object"!==typeof t.icons)return o;t.not_found instanceof Array&&t.not_found.forEach(t=>{e(t,null),o.push(t)});const r=t.icons;Object.keys(r).forEach(n=>{const r=u(t,n,!0);r&&(e(n,r),o.push(n))});const i=n.aliases||"all";if("none"!==i&&"object"===typeof t.aliases){const n=t.aliases;Object.keys(n).forEach(r=>{if("variations"===i&&f(n[r]))return;const c=u(t,r,!0);c&&(e(r,c),o.push(r))})}return o}const p={provider:"string",aliases:"object",not_found:"object"};for(const ie in i)p[ie]=typeof i[ie];function h(t){if("object"!==typeof t||null===t)return null;const e=t;if("string"!==typeof e.prefix||!t.icons||"object"!==typeof t.icons)return null;for(const r in p)if(void 0!==t[r]&&typeof t[r]!==p[r])return null;const n=e.icons;for(const c in n){const t=n[c];if(!c.match(r)||"string"!==typeof t.body)return null;for(const e in i)if(void 0!==t[e]&&typeof t[e]!==typeof i[e])return null}const o=e.aliases;if(o)for(const c in o){const t=o[c],e=t.parent;if(!c.match(r)||"string"!==typeof e||!n[e]&&!o[e])return null;for(const n in i)if(void 0!==t[n]&&typeof t[n]!==typeof i[n])return null}return e}const g=1;let b=Object.create(null);try{const t=window||self;t&&t._iconifyStorage.version===g&&(b=t._iconifyStorage.storage)}catch(oe){}function v(t,e){return{provider:t,prefix:e,icons:Object.create(null),missing:Object.create(null)}}function y(t,e){void 0===b[t]&&(b[t]=Object.create(null));const n=b[t];return void 0===n[e]&&(n[e]=v(t,e)),n[e]}function m(t,e){if(!h(e))return[];const n=Date.now();return d(e,(e,o)=>{o?t.icons[e]=o:t.missing[e]=n})}function x(t,e,n){try{if("string"===typeof n.body)return t.icons[e]=Object.freeze(c(n)),!0}catch(oe){}return!1}function w(t,e){const n=t.icons[e];return void 0===n?null:n}let j=!1;function k(t){return"boolean"===typeof t&&(j=t),j}function O(t){const e="string"===typeof t?s(t,!0,j):t;return e?w(y(e.provider,e.prefix),e.name):null}function I(t,e){const n=s(t,!0,j);if(!n)return!1;const o=y(n.provider,n.prefix);return x(o,n.name,e)}function E(t,e){if("object"!==typeof t)return!1;if("string"!==typeof e&&(e="string"===typeof t.provider?t.provider:""),j&&""===e&&("string"!==typeof t.prefix||""===t.prefix)){let e=!1;return h(t)&&(t.prefix="",d(t,(t,n)=>{n&&I(t,n)&&(e=!0)})),e}if("string"!==typeof t.prefix||!a({provider:e,prefix:t.prefix,name:"a"}))return!1;const n=y(e,t.prefix);return!!m(n,t)}const S=Object.freeze({inline:!1,width:null,height:null,hAlign:"center",vAlign:"middle",slice:!1,hFlip:!1,vFlip:!1,rotate:0});function A(t,e){const n={};for(const o in t){const r=o;if(n[r]=t[r],void 0===e[r])continue;const i=e[r];switch(r){case"inline":case"slice":"boolean"===typeof i&&(n[r]=i);break;case"hFlip":case"vFlip":!0===i&&(n[r]=!n[r]);break;case"hAlign":case"vAlign":"string"===typeof i&&""!==i&&(n[r]=i);break;case"width":case"height":("string"===typeof i&&""!==i||"number"===typeof i&&i||null===i)&&(n[r]=i);break;case"rotate":"number"===typeof i&&(n[r]+=i);break}}return n}const M=/(-?[0-9.]*[0-9]+[0-9.]*)/g,_=/^-?[0-9.]*[0-9]+[0-9.]*$/g;function F(t,e,n){if(1===e)return t;if(n=void 0===n?100:n,"number"===typeof t)return Math.ceil(t*e*n)/n;if("string"!==typeof t)return t;const o=t.split(M);if(null===o||!o.length)return t;const r=[];let i=o.shift(),c=_.test(i);while(1){if(c){const t=parseFloat(i);isNaN(t)?r.push(i):r.push(Math.ceil(t*e*n)/n)}else r.push(i);if(i=o.shift(),void 0===i)return r.join("");c=!c}}function T(t){let e="";switch(t.hAlign){case"left":e+="xMin";break;case"right":e+="xMax";break;default:e+="xMid"}switch(t.vAlign){case"top":e+="YMin";break;case"bottom":e+="YMax";break;default:e+="YMid"}return e+=t.slice?" slice":" meet",e}function L(t,e){const n={left:t.left,top:t.top,width:t.width,height:t.height};let o,r,i=t.body;[t,e].forEach(t=>{const e=[],o=t.hFlip,r=t.vFlip;let c,s=t.rotate;switch(o?r?s+=2:(e.push("translate("+(n.width+n.left).toString()+" "+(0-n.top).toString()+")"),e.push("scale(-1 1)"),n.top=n.left=0):r&&(e.push("translate("+(0-n.left).toString()+" "+(n.height+n.top).toString()+")"),e.push("scale(1 -1)"),n.top=n.left=0),s<0&&(s-=4*Math.floor(s/4)),s%=4,s){case 1:c=n.height/2+n.top,e.unshift("rotate(90 "+c.toString()+" "+c.toString()+")");break;case 2:e.unshift("rotate(180 "+(n.width/2+n.left).toString()+" "+(n.height/2+n.top).toString()+")");break;case 3:c=n.width/2+n.left,e.unshift("rotate(-90 "+c.toString()+" "+c.toString()+")");break}s%2===1&&(0===n.left&&0===n.top||(c=n.left,n.left=n.top,n.top=c),n.width!==n.height&&(c=n.width,n.width=n.height,n.height=c)),e.length&&(i='<g transform="'+e.join(" ")+'">'+i+"</g>")}),null===e.width&&null===e.height?(r="1em",o=F(r,n.width/n.height)):null!==e.width&&null!==e.height?(o=e.width,r=e.height):null!==e.height?(r=e.height,o=F(r,n.width/n.height)):(o=e.width,r=F(o,n.height/n.width)),"auto"===o&&(o=n.width),"auto"===r&&(r=n.height),o="string"===typeof o?o:o.toString()+"",r="string"===typeof r?r:r.toString()+"";const c={attributes:{width:o,height:r,preserveAspectRatio:T(e),viewBox:n.left.toString()+" "+n.top.toString()+" "+n.width.toString()+" "+n.height.toString()},body:i};return e.inline&&(c.inline=!0),c}const R=/\sid="(\S+)"/g,C="IconifyId"+Date.now().toString(16)+(16777216*Math.random()|0).toString(16);let D=0;function U(t,e=C){const n=[];let o;while(o=R.exec(t))n.push(o[1]);return n.length?(n.forEach(n=>{const o="function"===typeof e?e(n):e+(D++).toString(),r=n.replace(/[.*+?^${}()|[\]\\]/g,"\\$&");t=t.replace(new RegExp('([#;"])('+r+')([")]|\\.[a-z])',"g"),"$1"+o+"$3")}),t):t}const z=Object.create(null);function N(t,e){z[t]=e}function P(t){return z[t]||z[""]}function $(t){let e;if("string"===typeof t.resources)e=[t.resources];else if(e=t.resources,!(e instanceof Array)||!e.length)return null;const n={resources:e,path:void 0===t.path?"/":t.path,maxURL:t.maxURL?t.maxURL:500,rotate:t.rotate?t.rotate:750,timeout:t.timeout?t.timeout:5e3,random:!0===t.random,index:t.index?t.index:0,dataAfterTimeout:!1!==t.dataAfterTimeout};return n}const q=Object.create(null),J=["https://api.simplesvg.com","https://api.unisvg.com"],Y=[];while(J.length>0)1===J.length||Math.random()>.5?Y.push(J.shift()):Y.push(J.pop());function H(t,e){const n=$(e);return null!==n&&(q[t]=n,!0)}function B(t){return q[t]}q[""]=$({resources:["https://api.iconify.design"].concat(Y)});const V=(t,e)=>{let n=t,o=-1!==n.indexOf("?");function r(t){switch(typeof t){case"boolean":return t?"true":"false";case"number":return encodeURIComponent(t);case"string":return encodeURIComponent(t);default:throw new Error("Invalid parameter")}}return Object.keys(e).forEach(t=>{let i;try{i=r(e[t])}catch(oe){return}n+=(o?"&":"?")+encodeURIComponent(t)+"="+i,o=!0}),n},G={},K={},Q=()=>{let t;try{if(t=fetch,"function"===typeof t)return t}catch(oe){}return null};let W=Q();function X(t,e){const n=B(t);if(!n)return 0;let o;if(n.maxURL){let t=0;n.resources.forEach(e=>{const n=e;t=Math.max(t,n.length)});const r=V(e+".json",{icons:""});o=n.maxURL-t-n.path.length-r.length}else o=0;const r=t+":"+e;return K[t]=n.path,G[r]=o,o}function Z(t){return 404===t}const tt=(t,e,n)=>{const o=[];let r=G[e];void 0===r&&(r=X(t,e));const i="icons";let c={type:i,provider:t,prefix:e,icons:[]},s=0;return n.forEach((n,a)=>{s+=n.length+1,s>=r&&a>0&&(o.push(c),c={type:i,provider:t,prefix:e,icons:[]},s=n.length),c.icons.push(n)}),o.push(c),o};function et(t){if("string"===typeof t){if(void 0===K[t]){const e=B(t);if(!e)return"/";K[t]=e.path}return K[t]}return"/"}const nt=(t,e,n)=>{if(!W)return void n("abort",424);let o=et(e.provider);switch(e.type){case"icons":{const t=e.prefix,n=e.icons,r=n.join(",");o+=V(t+".json",{icons:r});break}case"custom":{const t=e.uri;o+="/"===t.slice(0,1)?t.slice(1):t;break}default:return void n("abort",400)}let r=503;W(t+o).then(t=>{const e=t.status;if(200===e)return r=501,t.json();setTimeout(()=>{n(Z(e)?"abort":"next",e)})}).then(t=>{"object"===typeof t&&null!==t?setTimeout(()=>{n("success",t)}):setTimeout(()=>{n("next",r)})}).catch(()=>{n("next",r)})},ot={prepare:tt,send:nt};function rt(t){const e={loaded:[],missing:[],pending:[]},n=Object.create(null);t.sort((t,e)=>t.provider!==e.provider?t.provider.localeCompare(e.provider):t.prefix!==e.prefix?t.prefix.localeCompare(e.prefix):t.name.localeCompare(e.name));let o={provider:"",prefix:"",name:""};return t.forEach(t=>{if(o.name===t.name&&o.prefix===t.prefix&&o.provider===t.provider)return;o=t;const r=t.provider,i=t.prefix,c=t.name;void 0===n[r]&&(n[r]=Object.create(null));const s=n[r];void 0===s[i]&&(s[i]=y(r,i));const a=s[i];let l;l=void 0!==a.icons[c]?e.loaded:""===i||void 0!==a.missing[c]?e.missing:e.pending;const u={provider:r,prefix:i,name:c};l.push(u)}),e}const it=Object.create(null),ct=Object.create(null);function st(t,e){t.forEach(t=>{const n=t.provider;if(void 0===it[n])return;const o=it[n],r=t.prefix,i=o[r];i&&(o[r]=i.filter(t=>t.id!==e))})}function at(t,e){void 0===ct[t]&&(ct[t]=Object.create(null));const n=ct[t];n[e]||(n[e]=!0,setTimeout(()=>{if(n[e]=!1,void 0===it[t]||void 0===it[t][e])return;const o=it[t][e].slice(0);if(!o.length)return;const r=y(t,e);let i=!1;o.forEach(n=>{const o=n.icons,c=o.pending.length;o.pending=o.pending.filter(n=>{if(n.prefix!==e)return!0;const c=n.name;if(void 0!==r.icons[c])o.loaded.push({provider:t,prefix:e,name:c});else{if(void 0===r.missing[c])return i=!0,!0;o.missing.push({provider:t,prefix:e,name:c})}return!1}),o.pending.length!==c&&(i||st([{provider:t,prefix:e}],n.id),n.callback(o.loaded.slice(0),o.missing.slice(0),o.pending.slice(0),n.abort))})}))}let lt=0;function ut(t,e,n){const o=lt++,r=st.bind(null,n,o);if(!e.pending.length)return r;const i={id:o,icons:e,callback:t,abort:r};return n.forEach(t=>{const e=t.provider,n=t.prefix;void 0===it[e]&&(it[e]=Object.create(null));const o=it[e];void 0===o[n]&&(o[n]=[]),o[n].push(i)}),r}function ft(t,e=!0,n=!1){const o=[];return t.forEach(t=>{const r="string"===typeof t?s(t,!1,n):t;e&&!a(r,n)||o.push({provider:r.provider,prefix:r.prefix,name:r.name})}),o}var dt={resources:[],index:0,timeout:2e3,rotate:750,random:!1,dataAfterTimeout:!1};function pt(t,e,n,o){const r=t.resources.length,i=t.random?Math.floor(Math.random()*r):t.index;let c;if(t.random){let e=t.resources.slice(0);c=[];while(e.length>1){const t=Math.floor(Math.random()*e.length);c.push(e[t]),e=e.slice(0,t).concat(e.slice(t+1))}c=c.concat(e)}else c=t.resources.slice(i).concat(t.resources.slice(0,i));const s=Date.now();let a,l="pending",u=0,f=null,d=[],p=[];function h(){f&&(clearTimeout(f),f=null)}function g(){"pending"===l&&(l="aborted"),h(),d.forEach(t=>{"pending"===t.status&&(t.status="aborted")}),d=[]}function b(t,e){e&&(p=[]),"function"===typeof t&&p.push(t)}function v(){return{startTime:s,payload:e,status:l,queriesSent:u,queriesPending:d.length,subscribe:b,abort:g}}function y(){l="failed",p.forEach(t=>{t(void 0,a)})}function m(){d.forEach(t=>{"pending"===t.status&&(t.status="aborted")}),d=[]}function x(e,n,o){const r="success"!==n;switch(d=d.filter(t=>t!==e),l){case"pending":break;case"failed":if(r||!t.dataAfterTimeout)return;break;default:return}if("abort"===n)return a=o,void y();if(r)return a=o,void(d.length||(c.length?w():y()));if(h(),m(),!t.random){const n=t.resources.indexOf(e.resource);-1!==n&&n!==t.index&&(t.index=n)}l="completed",p.forEach(t=>{t(o)})}function w(){if("pending"!==l)return;h();const o=c.shift();if(void 0===o)return d.length?void(f=setTimeout(()=>{h(),"pending"===l&&(m(),y())},t.timeout)):void y();const r={status:"pending",resource:o,callback:(t,e)=>{x(r,t,e)}};d.push(r),u++,f=setTimeout(w,t.rotate),n(o,e,r.callback)}return"function"===typeof o&&p.push(o),setTimeout(w),v}function ht(t){if("object"!==typeof t||"object"!==typeof t.resources||!(t.resources instanceof Array)||!t.resources.length)throw new Error("Invalid Reduncancy configuration");const e=Object.create(null);let n;for(n in dt)void 0!==t[n]?e[n]=t[n]:e[n]=dt[n];return e}function gt(t){const e=ht(t);let n=[];function o(){n=n.filter(t=>"pending"===t().status)}function r(t,r,i){const c=pt(e,t,r,(t,e)=>{o(),i&&i(t,e)});return n.push(c),c}function i(t){const e=n.find(e=>t(e));return void 0!==e?e:null}const c={query:r,find:i,setIndex:t=>{e.index=t},getIndex:()=>e.index,cleanup:o};return c}function bt(){}const vt=Object.create(null);function yt(t){if(void 0===vt[t]){const e=B(t);if(!e)return;const n=gt(e),o={config:e,redundancy:n};vt[t]=o}return vt[t]}function mt(t,e,n){let o,r;if("string"===typeof t){const e=P(t);if(!e)return n(void 0,424),bt;r=e.send;const i=yt(t);i&&(o=i.redundancy)}else{const e=$(t);if(e){o=gt(e);const n=t.resources?t.resources[0]:"",i=P(n);i&&(r=i.send)}}return o&&r?o.query(e,r,n)().abort:(n(void 0,424),bt)}const xt={};function wt(){}const jt=Object.create(null),kt=Object.create(null),Ot=Object.create(null),It=Object.create(null);function Et(t,e){void 0===Ot[t]&&(Ot[t]=Object.create(null));const n=Ot[t];n[e]||(n[e]=!0,setTimeout(()=>{n[e]=!1,at(t,e)}))}const St=Object.create(null);function At(t,e,n){function o(){const n=(""===t?"":"@"+t+":")+e,o=Math.floor(Date.now()/6e4);St[n]<o&&(St[n]=o,console.error('Unable to retrieve icons for "'+n+'" because API is not configured properly.'))}void 0===kt[t]&&(kt[t]=Object.create(null));const r=kt[t];void 0===It[t]&&(It[t]=Object.create(null));const i=It[t];void 0===jt[t]&&(jt[t]=Object.create(null));const c=jt[t];void 0===r[e]?r[e]=n:r[e]=r[e].concat(n).sort(),i[e]||(i[e]=!0,setTimeout(()=>{i[e]=!1;const n=r[e];delete r[e];const s=P(t);if(!s)return void o();const a=s.prepare(t,e,n);a.forEach(n=>{mt(t,n,(o,r)=>{const i=y(t,e);if("object"!==typeof o){if(404!==r)return;const t=Date.now();n.icons.forEach(e=>{i.missing[e]=t})}else try{const n=m(i,o);if(!n.length)return;const r=c[e];n.forEach(t=>{delete r[t]}),xt.store&&xt.store(t,o)}catch(s){console.error(s)}Et(t,e)})})}))}const Mt=(t,e)=>{const n=ft(t,!0,k()),o=rt(n);if(!o.pending.length){let t=!0;return e&&setTimeout(()=>{t&&e(o.loaded,o.missing,o.pending,wt)}),()=>{t=!1}}const r=Object.create(null),i=[];let c,s;o.pending.forEach(t=>{const e=t.provider,n=t.prefix;if(n===s&&e===c)return;c=e,s=n,i.push({provider:e,prefix:n}),void 0===jt[e]&&(jt[e]=Object.create(null));const o=jt[e];void 0===o[n]&&(o[n]=Object.create(null)),void 0===r[e]&&(r[e]=Object.create(null));const a=r[e];void 0===a[n]&&(a[n]=[])});const a=Date.now();return o.pending.forEach(t=>{const e=t.provider,n=t.prefix,o=t.name,i=jt[e][n];void 0===i[o]&&(i[o]=a,r[e][n].push(o))}),i.forEach(t=>{const e=t.provider,n=t.prefix;r[e][n].length&&At(e,n,r[e][n])}),e?ut(e,o,i):wt},_t="iconify2",Ft="iconify",Tt=Ft+"-count",Lt=Ft+"-version",Rt=36e5,Ct=168,Dt={local:!0,session:!0};let Ut=!1;const zt={local:0,session:0},Nt={local:[],session:[]};let Pt="undefined"===typeof window?{}:window;function $t(t){const e=t+"Storage";try{if(Pt&&Pt[e]&&"number"===typeof Pt[e].length)return Pt[e]}catch(oe){}return Dt[t]=!1,null}function qt(t,e,n){try{return t.setItem(Tt,n.toString()),zt[e]=n,!0}catch(oe){return!1}}function Jt(t){const e=t.getItem(Tt);if(e){const t=parseInt(e);return t||0}return 0}function Yt(t,e){try{t.setItem(Lt,_t)}catch(oe){}qt(t,e,0)}function Ht(t){try{const e=Jt(t);for(let n=0;n<e;n++)t.removeItem(Ft+n.toString())}catch(oe){}}const Bt=()=>{if(Ut)return;Ut=!0;const t=Math.floor(Date.now()/Rt)-Ct;function e(e){const n=$t(e);if(!n)return;const o=e=>{const o=Ft+e.toString(),r=n.getItem(o);if("string"!==typeof r)return!1;let i=!0;try{const e=JSON.parse(r);if("object"!==typeof e||"number"!==typeof e.cached||e.cached<t||"string"!==typeof e.provider||"object"!==typeof e.data||"string"!==typeof e.data.prefix)i=!1;else{const t=e.provider,n=e.data.prefix,o=y(t,n);i=m(o,e.data).length>0}}catch(oe){i=!1}return i||n.removeItem(o),i};try{const t=n.getItem(Lt);if(t!==_t)return t&&Ht(n),void Yt(n,e);let r=Jt(n);for(let n=r-1;n>=0;n--)o(n)||(n===r-1?r--:Nt[e].push(n));qt(n,e,r)}catch(oe){}}for(const n in Dt)e(n)},Vt=(t,e)=>{function n(n){if(!Dt[n])return!1;const o=$t(n);if(!o)return!1;let r=Nt[n].shift();if(void 0===r&&(r=zt[n],!qt(o,n,r+1)))return!1;try{const n={cached:Math.floor(Date.now()/Rt),provider:t,data:e};o.setItem(Ft+r.toString(),JSON.stringify(n))}catch(oe){return!1}return!0}Ut||Bt(),Object.keys(e.icons).length&&(e.not_found&&(e=Object.assign({},e),delete e.not_found),n("local")||n("session"))};const Gt=/[\s,]+/;function Kt(t,e){e.split(Gt).forEach(e=>{const n=e.trim();switch(n){case"horizontal":t.hFlip=!0;break;case"vertical":t.vFlip=!0;break}})}function Qt(t,e){e.split(Gt).forEach(e=>{const n=e.trim();switch(n){case"left":case"center":case"right":t.hAlign=n;break;case"top":case"middle":case"bottom":t.vAlign=n;break;case"slice":case"crop":t.slice=!0;break;case"meet":t.slice=!1}})}function Wt(t,e=0){const n=t.replace(/^-?[0-9.]*/,"");function o(t){while(t<0)t+=4;return t%4}if(""===n){const e=parseInt(t);return isNaN(e)?0:o(e)}if(n!==t){let e=0;switch(n){case"%":e=25;break;case"deg":e=90}if(e){let r=parseFloat(t.slice(0,t.length-n.length));return isNaN(r)?0:(r/=e,r%1===0?o(r):0)}}return e}const Xt={xmlns:"http://www.w3.org/2000/svg","xmlns:xlink":"http://www.w3.org/1999/xlink","aria-hidden":!0,role:"img"};let Zt={};["horizontal","vertical"].forEach(t=>{["Align","Flip"].forEach(e=>{const n=t.slice(0,1)+e,o={attr:n,boolean:"Flip"===e};Zt[t+"-"+e.toLowerCase()]=o,Zt[t.slice(0,1)+"-"+e.toLowerCase()]=o,Zt[t+e]=o})});const te=(t,e)=>{const n=A(S,e),r={...Xt};let i="object"!==typeof e.style||e.style instanceof Array?{}:{...e.style};for(let o in e){const t=e[o];if(void 0!==t)switch(o){case"icon":case"style":case"onLoad":break;case"inline":case"hFlip":case"vFlip":n[o]=!0===t||"true"===t||1===t;break;case"flip":"string"===typeof t&&Kt(n,t);break;case"align":"string"===typeof t&&Qt(n,t);break;case"color":i.color=t;break;case"rotate":"string"===typeof t?n[o]=Wt(t):"number"===typeof t&&(n[o]=t);break;case"ariaHidden":case"aria-hidden":!0!==t&&"true"!==t&&delete r["aria-hidden"];break;default:void 0!==Zt[o]?!Zt[o].boolean||!0!==t&&"true"!==t&&1!==t?Zt[o].boolean||"string"!==typeof t||""===t||(n[Zt[o].attr]=t):n[Zt[o].attr]=!0:void 0===S[o]&&(r[o]=t)}}const c=L(t,n);for(let o in c.attributes)r[o]=c.attributes[o];c.inline&&void 0===i.verticalAlign&&void 0===i["vertical-align"]&&(i.verticalAlign="-0.125em");let s=0,a=e.id;return"string"===typeof a&&(a=a.replace(/-/g,"_")),r["innerHTML"]=U(c.body,a?()=>a+"ID"+s++:"iconifyVue"),Object.keys(i).length>0&&(r["style"]=i),Object(o["h"])("svg",r)};if(k(!0),N("",ot),"undefined"!==typeof document&&"undefined"!==typeof window){xt.store=Vt,Bt();const t=window;if(void 0!==t.IconifyPreload){const e=t.IconifyPreload,n="Invalid IconifyPreload syntax.";"object"===typeof e&&null!==e&&(e instanceof Array?e:[e]).forEach(t=>{try{("object"!==typeof t||null===t||t instanceof Array||"object"!==typeof t.icons||"string"!==typeof t.prefix||!E(t))&&console.error(n)}catch(e){console.error(n)}})}if(void 0!==t.IconifyProviders){const e=t.IconifyProviders;if("object"===typeof e&&null!==e)for(let t in e){const n="IconifyProviders["+t+"] is invalid.";try{const o=e[t];if("object"!==typeof o||!o||void 0===o.resources)continue;H(t,o)||console.error(n)}catch(re){console.error(n)}}}}const ee=c({body:""}),ne=Object(o["defineComponent"])({inheritAttrs:!1,data(){return{iconMounted:!1,counter:0}},mounted(){this._name="",this._loadingIcon=null,this.iconMounted=!0},unmounted(){this.abortLoading()},methods:{abortLoading(){this._loadingIcon&&(this._loadingIcon.abort(),this._loadingIcon=null)},getIcon(t,e){if("object"===typeof t&&null!==t&&"string"===typeof t.body)return this._name="",this.abortLoading(),{data:c(t)};let n;if("string"!==typeof t||null===(n=s(t,!1,!0)))return this.abortLoading(),null;const o=O(n);if(null===o)return this._loadingIcon&&this._loadingIcon.name===t||(this.abortLoading(),this._name="",this._loadingIcon={name:t,abort:Mt([n],()=>{this.counter++})}),null;this.abortLoading(),this._name!==t&&(this._name=t,e&&e(t));const r=["iconify"];return""!==n.prefix&&r.push("iconify--"+n.prefix),""!==n.provider&&r.push("iconify--"+n.provider),{data:o,classes:r}}},render(){this.counter;const t=this.$attrs,e=this.iconMounted?this.getIcon(t.icon,t.onLoad):null;if(!e)return te(ee,t);let n=t;return e.classes&&(n={...t,class:("string"===typeof t["class"]?t["class"]+" ":"")+e.classes.join(" ")}),te(e.data,n)}})}}]);
//# sourceMappingURL=chunk-2d0c8dfa.cfce6616.js.map