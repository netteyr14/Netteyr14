<div align="center">

```
 █████╗ ██████╗ ██╗   ██╗██╗███╗   ██╗         ██╗ █████╗ ██╗   ██╗
██╔══██╗██╔══██╗██║   ██║██║████╗  ██║         ██║██╔══██╗╚██╗ ██╔╝
███████║██████╔╝██║   ██║██║██╔██╗ ██║         ██║███████║ ╚████╔╝ 
██╔══██║██╔══██╗╚██╗ ██╔╝██║██║╚██╗██║    ██   ██║██╔══██║  ╚██╔╝  
██║  ██║██║  ██║ ╚████╔╝ ██║██║ ╚████║    ╚█████╔╝██║  ██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝     ╚════╝ ╚═╝  ╚═╝   ╚═╝  
```

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=16&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=BSIT+Student+%40+Colegio+de+Sta.+Teresa+de+Avila;Building+systems+that+matter+in+the+real+world;IoT+%7C+Machine+Learning+%7C+Full-Stack+Development;Currently+shipping%3A+FloodWatch+%F0%9F%8C%8A)](https://github.com/netteyr14)

[![Profile Views](https://komarev.com/ghpvc/?username=netteyr14&style=flat-square&color=58A6FF&label=profile+views)](https://github.com/netteyr14)
&nbsp;
[![GitHub followers](https://img.shields.io/github/followers/netteyr14?style=flat-square&color=58A6FF&label=followers)](https://github.com/netteyr14?tab=followers)
&nbsp;
[![GitHub Stars](https://img.shields.io/badge/dynamic/json?style=flat-square&color=58A6FF&label=total%20stars&query=%24.stars&url=https://api.github-star-counter.workers.dev/user/netteyr14)](https://github.com/netteyr14)

</div>

---

## `> whoami`

```python
arvin = {
    "name"      : "Isorena, Arvin Jay",
    "alias"     : ["netteyr14", "sheeshkebab"],
    "degree"    : "BS Information Technology — 3rd Year",
    "school"    : "Colegio de Sta. Teresa de Avila",
    "location"  : "Philippines 🇵🇭  (UTC +08:00)",
    "focus"     : ["IoT Systems", "ML Forecasting", "Full-Stack Dev"],
    "currently" : "Building FloodWatch 🌊 — a LoRaWAN flood monitoring system",
    "contact"   : "753951852456arvin@gmail.com",
}
```

> *"I build software that solves real problems — not just things that look cool in a browser."*

---

## `> stack --list`

<div align="center">

**Languages**

![Python](https://img.shields.io/badge/Python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![C#](https://img.shields.io/badge/C%23-%23239120.svg?style=for-the-badge&logo=c-sharp&logoColor=white)
![Java](https://img.shields.io/badge/Java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)
![Dart](https://img.shields.io/badge/Dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white)

**Frameworks & Tools**

![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=flutter&logoColor=white)
![React](https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![NGINX](https://img.shields.io/badge/NGINX-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-9B59B6?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

</div>

---

## `> projects --featured`

<div align="center">

### 🌊 FloodWatch &nbsp;&nbsp; <sub><sup>`capstone · under active development`</sup></sub>

**Real-Time Flood Monitoring & Water Level Forecasting System**

**Deployed for:** Barangay 178, Camarin, Caloocan City &nbsp;|&nbsp; **Adviser:** Harold Lucero, DIT

</div>

> FloodWatch is a production-grade community flood monitoring system built end-to-end — from custom LoRaWAN radio hardware to a cross-platform Flutter app. It transmits real-time sensor data over low-power RF, runs a trained LightGBM model to forecast water level trends, and delivers live alerts to residents and barangay officials — all containerized and load-tested.

<br/>

**`// End-to-End System Pipeline`**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        F L O O D W A T C H                               │
│                  Real-Time Flood Monitoring System                       │
└──────────────────────────────────────────────────────────────────────────┘

  [ FIELD LAYER ]              [ GATEWAY LAYER ]         [ SERVER LAYER ]

  ┌─────────────┐  LoRa RF    ┌──────────────┐  LAN    ┌──────────────────────────────────┐
  │ LoRa32 Node │ ──────────► │ LoRa32 SCPf  │ ──────► │        Docker Compose            │
  │ (Sensor     │ Sub-GHz     │ (Single-Chan  │         │  ┌─────────────────────────────┐ │
  │  Tower)     │             │  Pkt Forwarder│         │  │   NGINX  (Rate Limiter)     │ │
  │             │             │               │         │  │   per-location enforcement  │ │
  │ · Ultrasonic│             │ · Bridges RF  │         │  └──────────────┬──────────────┘ │
  │   water lvl │             │   to IP stack │         │                 │                │
  │ · Transmits │             │ · Forwards    │         │  ┌──────────────▼──────────────┐ │
  │   over LoRa │             │   LoRa pkts   │         │  │     Flask API  (Python)     │ │
  └─────────────┘             └───────────────┘         │  │  ┌────────┬────────┬──────┐ │ │
                                                         │  │  │ Admin  │ Tower  │  ML  │ │ │
                                                         │  │  │ Routes │ Routes │Routes│ │ │
                                                         │  │  └───┬────┴───┬────┴───┬──┘ │ │
                                                         │  └──────┼────────┼────────┼────┘ │
                                                         │         │        │        │       │
                                                         │  ┌──────▼──┐   ┌─▼────────▼────┐ │
                                                         │  │  MySQL  │   │  LightGBM ML  │ │
                                                         │  │  (DB)   │   │ Forecast Model│ │
                                                         │  └─────────┘   └───────────────┘ │
                                                         └──────────────────┬───────────────┘
                                                                            │
                                                               ┌────────────▼───────────┐
                                                               │    Flutter Frontend     │
                                                               │  📱 Mobile  (Android)  │
                                                               │  🖥️  Desktop (Windows) │
                                                               │  🌐 Web    (Browser)   │
                                                               └────────────────────────┘
```

<br/>

**`// Engineering highlights`**

<table>
  <tr>
    <td>📡 &nbsp;<b>LoRaWAN WSN</b></td>
    <td>Two LoRa32 boards — one as a field sensor tower transmitting raw water level readings over Sub-GHz LoRa RF, the other acting as a single-channel packet forwarder that bridges the radio link to the LAN stack. Zero cloud dependency on the RF hop.</td>
  </tr>
  <tr>
    <td>🧠 &nbsp;<b>LightGBM Forecasting</b></td>
    <td>Trained ML model predicting water level trends from historical sensor data, isolated behind its own <code>/ml</code> API route — fully decoupled from sensor ingestion and admin logic to keep each service independently scalable.</td>
  </tr>
  <tr>
    <td>🐳 &nbsp;<b>Dockerized & Resource-Scoped</b></td>
    <td>Fully containerized with Docker Compose. Every service (API, DB, NGINX) carries its own CPU and memory ceiling — no single container can starve the system under surge load.</td>
  </tr>
  <tr>
    <td>🛡️ &nbsp;<b>Per-Location Rate Limiting</b></td>
    <td>NGINX enforces rate limits scoped per source location — protecting the API against both accidental burst traffic and deliberate abuse without standing up a full WAF.</td>
  </tr>
  <tr>
    <td>📊 &nbsp;<b>Dual Load Testing</b></td>
    <td><b>k6</b> for distributed multi-IP concurrent user simulation. <b>Locust</b> for single abusive-IP stress testing. Both used to validate backend resilience against real-world community traffic scenarios and identify throughput ceilings per container.</td>
  </tr>
  <tr>
    <td>📱 &nbsp;<b>Cross-Platform Flutter</b></td>
    <td>One codebase targeting Android mobile, Windows desktop, and browser — designed for both smartphones of barangay residents and fixed command-center dashboards used by officials during flood events.</td>
  </tr>
</table>

<br/>

<div align="center">

![Python](https://img.shields.io/badge/Python-backend-3776AB?style=flat-square&logo=python&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-cross--platform-02569B?style=flat-square&logo=flutter&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-containerized-0db7ed?style=flat-square&logo=docker&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-forecasting-9B59B6?style=flat-square)
![NGINX](https://img.shields.io/badge/NGINX-rate--limited-009639?style=flat-square&logo=nginx&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-timeseries--data-4479A1?style=flat-square&logo=mysql&logoColor=white)
![LoRaWAN](https://img.shields.io/badge/LoRaWAN-Sub--GHz%20WSN-2ecc71?style=flat-square)
![k6](https://img.shields.io/badge/k6-load--tested-7D64FF?style=flat-square&logo=k6&logoColor=white)

<a href="https://github.com/netteyr14/FloodWatch">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=netteyr14&repo=FloodWatch&theme=github_dark&hide_border=true" />
</a>

</div>

---

## `> stats --verbose`

<div align="center">

> ⚠️ **Note:** FloodWatch repos are kept **private** (pending commercialization with the client barangay). Stats reflect public activity only.

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com?user=netteyr14&theme=github-dark-blue&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" width="49%"/>
<img src="https://github-readme-stats.vercel.app/api?username=netteyr14&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true&rank_icon=github" width="49%"/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=netteyr14&layout=compact&theme=github_dark&hide_border=true&langs_count=8&count_private=true" width="45%"/>

</div>

---

## `> activity --graph`

<div align="center">

[![Contribution Graph](https://github-readme-activity-graph.vercel.app/graph?username=netteyr14&bg_color=0d1117&color=58A6FF&line=58A6FF&point=ffffff&area=true&hide_border=true&custom_title=Arvin's%20Contribution%20Activity)](https://github.com/netteyr14)

</div>

---

## `> contact --reach-out`

<div align="center">

[![Facebook](https://img.shields.io/badge/Facebook-Arvin%20Jay%20Isorena-%231877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/m.Arvin.Jay.isorena.27)
&nbsp;
[![Email](https://img.shields.io/badge/Email-Say%20Hello-%23EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:753951852456arvin@gmail.com)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-netteyr14-%23181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/netteyr14)

<br/>

```
// Need access to private repos (backend, mobile, admin dashboard)?
// → Reach out via email — happy to share for research or collaboration.
```

<br/>

![footer](https://capsule-render.vercel.app/api?type=waving&color=58A6FF&height=80&section=footer)

</div>
