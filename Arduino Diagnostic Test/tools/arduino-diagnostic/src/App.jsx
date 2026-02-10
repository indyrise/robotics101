import { useState, useEffect, useRef, useCallback } from "react";

const QUESTIONS = [
  { id:1, cat:"Electricity", q:"What is the unit of electrical resistance?", opts:["Ampere","Ohm","Volt","Watt"], ans:1, std:"CSTA 2-CS-02 | NGSS MS-PS2-3" },
  { id:2, cat:"Electricity", q:"A 9V battery is connected to a 300Ω resistor. What is the current?", opts:["0.3A","0.003A","0.03A","3A"], ans:2, std:"CSTA 2-DA-08 | NGSS MS-PS2-3" },
  { id:3, cat:"Electricity", q:"Which best describes capacitance?", opts:["Opposition to current flow","Ability to store electrical charge","Rate at which charge flows","Force that pushes electrons"], ans:1, std:"CSTA 2-CS-02 | NGSS MS-PS2-5" },
  { id:4, cat:"Circuits & Schematics", q:"In a circuit schematic, what does a zigzag line typically represent?", opts:["Capacitor","Inductor","Resistor","Diode"], ans:2, std:"CSTA 2-CS-02 | NGSS MS-ETS1-1" },
  { id:5, cat:"Circuits & Schematics", q:"Three 100Ω resistors in series — total resistance?", opts:["33.3Ω","100Ω","200Ω","300Ω"], ans:3, std:"CSTA 2-DA-08 | NGSS MS-PS2-3" },
  { id:6, cat:"Arduino Boards", q:"How many digital I/O pins does the Arduino Uno have?", opts:["6","14","20","32"], ans:1, std:"CSTA 2-CS-01 | NGSS MS-ETS1-4" },
  { id:7, cat:"Arduino Boards", q:"Which is NOT a feature of the Arduino Uno?", opts:["ATmega328P microcontroller","USB connection","Built-in Wi-Fi module","16 MHz clock speed"], ans:2, std:"CSTA 2-CS-01 | NGSS MS-ETS1-1" },
  { id:8, cat:"Arduino Boards", q:"What voltage does the Arduino Uno operate at?", opts:["5V","3.3V","9V","12V"], ans:0, std:"CSTA 2-CS-02 | NGSS MS-PS2-3" },
  { id:9, cat:"Arduino IDE", q:"What are the two required functions in every Arduino sketch?", opts:["begin() and end()","setup() and loop()","start() and stop()","init() and run()"], ans:1, std:"CSTA 2-AP-13 | NGSS MS-ETS1-2" },
  { id:10, cat:"Arduino IDE", q:"What does the Serial Monitor allow you to do?", opts:["Upload sketches faster","Change board type","Adjust pin voltage","View data sent from Arduino to computer"], ans:3, std:"CSTA 2-AP-17 | NGSS MS-ETS1-3" },
  { id:11, cat:"Arduino IDE", q:"What baud rate is most commonly used with Serial.begin()?", opts:["4800","2400","9600","115200"], ans:2, std:"CSTA 2-AP-17 | NGSS MS-ETS1-3" },
  { id:12, cat:"Electronic Components", q:"What is the purpose of a resistor in an LED circuit?", opts:["Increase brightness","Limit current and prevent burnout","Store energy","Switch the LED on/off"], ans:1, std:"CSTA 2-CS-02 | NGSS MS-PS2-3" },
  { id:13, cat:"Electronic Components", q:"Which component converts light into an electrical signal?", opts:["Piezo buzzer","Servo motor","Photoresistor (LDR)","Relay"], ans:2, std:"CSTA 2-CS-01 | NGSS MS-PS4-2" },
  { id:14, cat:"Electronic Components", q:"An LED's longer leg is the:", opts:["Anode (positive)","Cathode (negative)","Ground","Signal"], ans:0, std:"CSTA 2-CS-02 | NGSS MS-ETS1-1" },
  { id:15, cat:"Electronic Components", q:"What type of motor allows precise angular positioning?", opts:["DC motor","Stepper motor","Brushless motor","Servo motor"], ans:3, std:"CSTA 2-CS-01 | NGSS MS-PS2-2" },
  { id:16, cat:"Programming Syntax", q:"Which data type stores a decimal number in Arduino?", opts:["int","float","char","boolean"], ans:1, std:"CSTA 2-AP-11 | NGSS MS-ETS1-4" },
  { id:17, cat:"Programming Syntax", q:"What does: for(int i = 0; i < 5; i++) { } do?", opts:["Runs once","Runs indefinitely","Repeats 5 times","Repeats 4 times"], ans:2, std:"CSTA 2-AP-12 | NGSS MS-ETS1-4" },
  { id:18, cat:"Programming Syntax", q:"What symbol is used for single-line comments in Arduino?", opts:["//","/* */","#","<!-- -->"], ans:0, std:"CSTA 2-AP-19 | NGSS MS-ETS1-2" },
  { id:19, cat:"Programming Syntax", q:"Which correctly declares a constant in Arduino?", opts:["var ledPin = 13;","int ledPin == 13;","define ledPin 13","const int ledPin = 13;"], ans:3, std:"CSTA 2-AP-11 | NGSS MS-ETS1-1" },
  { id:20, cat:"Programming Logic", q:"What does digitalRead(pin) return?", opts:["A value 0–1023","HIGH or LOW","A voltage value","The pin number"], ans:1, std:"CSTA 2-AP-10 | NGSS MS-PS4-2" },
  { id:21, cat:"Programming Logic", q:"What is the output range of analogRead() on Arduino Uno?", opts:["0–100","0–255","0–1023","0–4095"], ans:2, std:"CSTA 2-DA-08 | NGSS MS-PS4-2" },
  { id:22, cat:"Programming Logic", q:'if(digitalRead(2)==HIGH){digitalWrite(13,HIGH);}else{digitalWrite(13,LOW);} — What does this do?', opts:["Turns on LED at pin 13 when button at pin 2 is pressed","Blinks an LED","Reads a sensor value","Creates a delay"], ans:0, std:"CSTA 2-AP-12 | NGSS MS-ETS1-4" },
  { id:23, cat:"PWM & Frequency", q:"What does PWM stand for?", opts:["Pulse Width Modulation","Power Wave Modification","Pulse Wave Management","Pin Width Measure"], ans:0, std:"CSTA 2-CS-02 | NGSS MS-PS4-1" },
  { id:24, cat:"PWM & Frequency", q:"If a PWM signal has a 50% duty cycle, what is the analogWrite() value?", opts:["50","100","≈127","200"], ans:2, std:"CSTA 2-DA-08 | NGSS MS-PS4-1" },
  { id:25, cat:"Circuits & Schematics", q:"On a breadboard, which rows are connected along the full length?", opts:["The power rails (+ and −)","All center rows","Only the top row","None"], ans:0, std:"CSTA 2-CS-02 | NGSS MS-ETS1-1" },
  { id:26, cat:"Programming Logic", q:"What is the purpose of the delay() function?", opts:["Stops program permanently","Resets the Arduino","Reads a sensor","Pauses execution for specified milliseconds"], ans:3, std:"CSTA 2-AP-12 | NGSS MS-ETS1-4" },
  { id:27, cat:"Electronic Components", q:"A potentiometer is an example of a:", opts:["Digital sensor","Variable resistor","Capacitor","Transistor"], ans:1, std:"CSTA 2-CS-01 | NGSS MS-PS2-3" },
  { id:28, cat:"Electricity", q:"Power (in watts) is calculated as:", opts:["Voltage ÷ Current","Resistance × Current","Voltage × Current","Resistance ÷ Voltage"], ans:2, std:"CSTA 2-DA-08 | NGSS MS-PS2-3" },
  { id:29, cat:"Arduino IDE", q:"What happens when you click Verify (✓) in the Arduino IDE?", opts:["Code is compiled and checked for errors","Code uploads to board","Serial Monitor opens","Board resets"], ans:0, std:"CSTA 2-AP-17 | NGSS MS-ETS1-3" },
  { id:30, cat:"Programming Syntax", q:"Correct syntax to set pin 9 as an output?", opts:["pin(9, OUTPUT);","pinMode(9, OUTPUT);","setPin(9, OUT);","output(9);"], ans:1, std:"CSTA 2-AP-13 | NGSS MS-ETS1-1" },
  { id:31, cat:"Programming Logic", q:"What value range does analogWrite() accept?", opts:["0–1023","HIGH or LOW","TRUE or FALSE","0–255"], ans:3, std:"CSTA 2-AP-11 | NGSS MS-PS4-1" },
  { id:32, cat:"Electronic Components", q:"A piezo buzzer converts:", opts:["Electrical signals to sound","Sound to electrical signals","Light to electrical signals","Heat to electrical signals"], ans:0, std:"CSTA 2-CS-01 | NGSS MS-PS4-1" },
  { id:33, cat:"PWM & Frequency", q:"Which Arduino Uno pins support PWM output?", opts:["All digital pins","Only analog pins","Pins marked with ~ (3,5,6,9,10,11)","Only pins 0 and 1"], ans:2, std:"CSTA 2-CS-02 | NGSS MS-PS4-1" },
  { id:34, cat:"Arduino Boards", q:"How many analog input pins does the Arduino Uno have?", opts:["4","6","8","14"], ans:1, std:"CSTA 2-CS-01 | NGSS MS-ETS1-1" },
  { id:35, cat:"Electricity", q:"In Ohm's Law (V=IR), doubling resistance at constant voltage does what to current?", opts:["Halves it","Doubles it","No change","Quadruples it"], ans:0, std:"CSTA 2-DA-08 | NGSS MS-PS2-3" },
  { id:36, cat:"Programming Logic", q:"int x=10; while(x>0){x=x-3;} Serial.println(x); — What prints?", opts:["0","1","-2","3"], ans:2, std:"CSTA 2-AP-12 | NGSS MS-ETS1-4" },
];

const CATEGORIES = ["Electricity","Circuits & Schematics","Arduino Boards","Arduino IDE","Electronic Components","Programming Syntax","Programming Logic","PWM & Frequency"];
const CAT_COLORS = {"Electricity":"#E8913A","Circuits & Schematics":"#5B8DBE","Arduino Boards":"#00979D","Arduino IDE":"#6B5B95","Electronic Components":"#D35B5B","Programming Syntax":"#2D8659","Programming Logic":"#C4793A","PWM & Frequency":"#8B6DAF"};
const TOTAL_TIME = 75 * 60;

const letters = ["A","B","C","D"];

export default function ArduinoDiagnostic() {
  const [phase, setPhase] = useState("start");
  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState({});
  const [flagged, setFlagged] = useState(new Set());
  const [timeLeft, setTimeLeft] = useState(TOTAL_TIME);
  const [showNav, setShowNav] = useState(false);
  const timerRef = useRef(null);

  useEffect(() => {
    if (phase === "test") {
      timerRef.current = setInterval(() => {
        setTimeLeft(t => {
          if (t <= 1) { clearInterval(timerRef.current); setPhase("results"); return 0; }
          return t - 1;
        });
      }, 1000);
      return () => clearInterval(timerRef.current);
    }
  }, [phase]);

  const formatTime = (s) => {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}:${sec.toString().padStart(2, "0")}`;
  };

  const select = useCallback((qi, oi) => {
    setAnswers(prev => ({ ...prev, [qi]: oi }));
  }, []);

  const toggleFlag = useCallback((qi) => {
    setFlagged(prev => {
      const n = new Set(prev);
      n.has(qi) ? n.delete(qi) : n.add(qi);
      return n;
    });
  }, []);

  const submit = () => {
    clearInterval(timerRef.current);
    setPhase("results");
  };

  const getScore = () => {
    let correct = 0;
    const catScores = {};
    CATEGORIES.forEach(c => catScores[c] = { correct: 0, total: 0 });
    QUESTIONS.forEach((q, i) => {
      catScores[q.cat].total++;
      if (answers[i] === q.ans) { correct++; catScores[q.cat].correct++; }
    });
    return { correct, total: QUESTIONS.length, pct: Math.round(correct / QUESTIONS.length * 100), catScores };
  };

  const timeWarning = timeLeft < 300;
  const timeCritical = timeLeft < 60;
  const answered = Object.keys(answers).length;
  const q = QUESTIONS[current];

  // START SCREEN
  if (phase === "start") {
    return (
      <div style={{ minHeight:"100vh", background:"linear-gradient(145deg, #0a1628 0%, #122040 40%, #1a2d52 100%)", display:"flex", alignItems:"center", justifyContent:"center", fontFamily:"'JetBrains Mono', 'SF Mono', 'Fira Code', monospace", padding:"20px" }}>
        <div style={{ maxWidth:560, width:"100%", textAlign:"center" }}>
          <div style={{ fontSize:13, letterSpacing:6, color:"#00979D", marginBottom:12, textTransform:"uppercase", fontWeight:600 }}>Arduino Certification</div>
          <div style={{ fontSize:32, fontWeight:800, color:"#E8E6E3", lineHeight:1.2, marginBottom:8 }}>Diagnostic Exam</div>
          <div style={{ width:60, height:3, background:"#00979D", margin:"16px auto 24px", borderRadius:2 }}/>
          <div style={{ color:"#8B9DC3", fontSize:14, lineHeight:1.7, marginBottom:32 }}>
            36 questions across 8 categories matching the official Arduino Fundamentals Certification. You have 75 minutes. Navigate freely between questions. Flag items to review before submitting.
          </div>
          <div style={{ display:"grid", gridTemplateColumns:"repeat(2, 1fr)", gap:8, marginBottom:32, textAlign:"left" }}>
            {CATEGORIES.map(c => (
              <div key={c} style={{ display:"flex", alignItems:"center", gap:8, padding:"6px 10px", background:"rgba(255,255,255,0.03)", borderRadius:6, border:"1px solid rgba(255,255,255,0.06)" }}>
                <div style={{ width:8, height:8, borderRadius:2, background:CAT_COLORS[c], flexShrink:0 }}/>
                <span style={{ color:"#C0CAD8", fontSize:11.5 }}>{c}</span>
              </div>
            ))}
          </div>
          <button onClick={() => setPhase("test")} style={{ padding:"14px 48px", background:"#00979D", color:"#fff", border:"none", borderRadius:8, fontSize:15, fontWeight:700, cursor:"pointer", fontFamily:"inherit", letterSpacing:1, transition:"all 0.2s" }}
            onMouseOver={e => e.target.style.background="#00B4B8"}
            onMouseOut={e => e.target.style.background="#00979D"}>
            BEGIN EXAM
          </button>
          <div style={{ color:"#556B8A", fontSize:11, marginTop:16 }}>Source: arduino.cc/education/certification</div>
        </div>
      </div>
    );
  }

  // RESULTS SCREEN
  if (phase === "results") {
    const score = getScore();
    const band = score.pct >= 90 ? { label:"Certification Ready", color:"#2D8659", msg:"Review any missed items, then schedule your exam." }
      : score.pct >= 75 ? { label:"Almost There", color:"#C4793A", msg:"Focus on weak categories using the Arduino Starter Kit projects." }
      : score.pct >= 60 ? { label:"More Practice Needed", color:"#D35B5B", msg:"Work through all 15 Starter Kit projects before testing." }
      : { label:"Start from Scratch", color:"#8B3A3A", msg:"Begin with the Starter Kit project book from Project 1." };

    return (
      <div style={{ minHeight:"100vh", background:"linear-gradient(145deg, #0a1628 0%, #122040 40%, #1a2d52 100%)", fontFamily:"'JetBrains Mono', 'SF Mono', 'Fira Code', monospace", padding:"24px", color:"#E8E6E3" }}>
        <div style={{ maxWidth:720, margin:"0 auto" }}>
          <div style={{ textAlign:"center", marginBottom:32 }}>
            <div style={{ fontSize:13, letterSpacing:4, color:"#00979D", marginBottom:8, textTransform:"uppercase" }}>Exam Complete</div>
            <div style={{ fontSize:64, fontWeight:800, color:band.color }}>{score.pct}%</div>
            <div style={{ fontSize:18, fontWeight:700, color:band.color, marginBottom:4 }}>{band.label}</div>
            <div style={{ color:"#8B9DC3", fontSize:13 }}>{score.correct} of {score.total} correct — {band.msg}</div>
            <div style={{ color:"#556B8A", fontSize:11, marginTop:4 }}>Time used: {formatTime(TOTAL_TIME - timeLeft)}</div>
          </div>

          {/* Category breakdown */}
          <div style={{ background:"rgba(255,255,255,0.03)", borderRadius:12, border:"1px solid rgba(255,255,255,0.08)", padding:20, marginBottom:24 }}>
            <div style={{ fontSize:12, letterSpacing:3, color:"#8B9DC3", marginBottom:16, textTransform:"uppercase" }}>Category Breakdown</div>
            {CATEGORIES.map(cat => {
              const cs = score.catScores[cat];
              const pct = cs.total > 0 ? Math.round(cs.correct / cs.total * 100) : 0;
              return (
                <div key={cat} style={{ marginBottom:12 }}>
                  <div style={{ display:"flex", justifyContent:"space-between", marginBottom:4 }}>
                    <span style={{ fontSize:12.5, color:"#C0CAD8" }}>{cat}</span>
                    <span style={{ fontSize:12.5, color: pct >= 75 ? "#2D8659" : pct >= 50 ? "#C4793A" : "#D35B5B", fontWeight:600 }}>{cs.correct}/{cs.total} ({pct}%)</span>
                  </div>
                  <div style={{ height:6, background:"rgba(255,255,255,0.06)", borderRadius:3, overflow:"hidden" }}>
                    <div style={{ width:`${pct}%`, height:"100%", background: pct >= 75 ? "#2D8659" : pct >= 50 ? "#C4793A" : "#D35B5B", borderRadius:3, transition:"width 0.5s ease" }}/>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Question review */}
          <div style={{ background:"rgba(255,255,255,0.03)", borderRadius:12, border:"1px solid rgba(255,255,255,0.08)", padding:20 }}>
            <div style={{ fontSize:12, letterSpacing:3, color:"#8B9DC3", marginBottom:16, textTransform:"uppercase" }}>Question Review</div>
            {QUESTIONS.map((qq, i) => {
              const userAns = answers[i];
              const isCorrect = userAns === qq.ans;
              const unanswered = userAns === undefined;
              return (
                <div key={i} style={{ padding:"10px 12px", borderRadius:8, marginBottom:6, background: isCorrect ? "rgba(45,134,89,0.1)" : "rgba(211,91,91,0.1)", border:`1px solid ${isCorrect ? "rgba(45,134,89,0.2)" : "rgba(211,91,91,0.2)"}` }}>
                  <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-start", gap:8 }}>
                    <div style={{ flex:1 }}>
                      <span style={{ fontSize:12, color: isCorrect ? "#2D8659" : "#D35B5B", fontWeight:700 }}>Q{qq.id} {isCorrect ? "✓" : "✗"}</span>
                      <span style={{ fontSize:11.5, color:"#8B9DC3", marginLeft:8 }}>{qq.q.slice(0, 70)}{qq.q.length > 70 ? "…" : ""}</span>
                    </div>
                    <div style={{ textAlign:"right", flexShrink:0 }}>
                      {!isCorrect && <div style={{ fontSize:11, color:"#D35B5B" }}>{unanswered ? "No answer" : `You: ${letters[userAns]}`}</div>}
                      {!isCorrect && <div style={{ fontSize:11, color:"#2D8659" }}>Correct: {letters[qq.ans]}) {qq.opts[qq.ans]}</div>}
                    </div>
                  </div>
                  {!isCorrect && <div style={{ fontSize:10.5, color:"#556B8A", marginTop:4 }}>{qq.std}</div>}
                </div>
              );
            })}
          </div>

          {/* Standards summary */}
          <div style={{ marginTop:24, padding:16, background:"rgba(255,255,255,0.03)", borderRadius:12, border:"1px solid rgba(255,255,255,0.08)" }}>
            <div style={{ fontSize:12, letterSpacing:3, color:"#8B9DC3", marginBottom:12, textTransform:"uppercase" }}>Aligned Standards</div>
            <div style={{ fontSize:11, color:"#8B9DC3", lineHeight:1.8 }}>
              <div><span style={{color:"#00979D", fontWeight:600}}>CSTA:</span> 2-CS-01, 2-CS-02, 2-AP-10, 2-AP-11, 2-AP-12, 2-AP-13, 2-AP-17, 2-AP-19, 2-DA-08</div>
              <div><span style={{color:"#00979D", fontWeight:600}}>NGSS:</span> MS-PS2-2, MS-PS2-3, MS-PS2-5, MS-PS4-1, MS-PS4-2, MS-ETS1-1, MS-ETS1-2, MS-ETS1-3, MS-ETS1-4</div>
            </div>
          </div>

          <div style={{ textAlign:"center", marginTop:24 }}>
            <button onClick={() => { setPhase("start"); setCurrent(0); setAnswers({}); setFlagged(new Set()); setTimeLeft(TOTAL_TIME); }}
              style={{ padding:"12px 36px", background:"#00979D", color:"#fff", border:"none", borderRadius:8, fontSize:13, fontWeight:700, cursor:"pointer", fontFamily:"inherit" }}>
              RETAKE EXAM
            </button>
          </div>
        </div>
      </div>
    );
  }

  // TEST SCREEN
  return (
    <div style={{ minHeight:"100vh", background:"linear-gradient(145deg, #0a1628 0%, #122040 40%, #1a2d52 100%)", fontFamily:"'JetBrains Mono', 'SF Mono', 'Fira Code', monospace", color:"#E8E6E3" }}>
      {/* Top bar */}
      <div style={{ position:"sticky", top:0, zIndex:10, background:"rgba(10,22,40,0.95)", backdropFilter:"blur(12px)", borderBottom:"1px solid rgba(255,255,255,0.06)", padding:"10px 20px", display:"flex", justifyContent:"space-between", alignItems:"center" }}>
        <div style={{ display:"flex", alignItems:"center", gap:16 }}>
          <div style={{ fontSize:12, color:"#8B9DC3" }}>
            <span style={{ color:"#00979D", fontWeight:700 }}>{answered}</span>/{QUESTIONS.length} answered
          </div>
          <div style={{ fontSize:12, color: flagged.size > 0 ? "#E8913A" : "#556B8A" }}>
            {flagged.size > 0 ? `⚑ ${flagged.size} flagged` : ""}
          </div>
        </div>
        <div style={{ fontSize:18, fontWeight:800, fontVariantNumeric:"tabular-nums", color: timeCritical ? "#D35B5B" : timeWarning ? "#E8913A" : "#E8E6E3", animation: timeCritical ? "pulse 1s infinite" : "none" }}>
          {formatTime(timeLeft)}
        </div>
        <div style={{ display:"flex", gap:8 }}>
          <button onClick={() => setShowNav(!showNav)} style={{ padding:"6px 14px", background:"rgba(255,255,255,0.06)", color:"#C0CAD8", border:"1px solid rgba(255,255,255,0.1)", borderRadius:6, fontSize:11, cursor:"pointer", fontFamily:"inherit" }}>
            {showNav ? "Hide" : "Nav"} ☰
          </button>
          <button onClick={submit} style={{ padding:"6px 14px", background: answered === QUESTIONS.length ? "#00979D" : "rgba(255,255,255,0.06)", color: answered === QUESTIONS.length ? "#fff" : "#8B9DC3", border:"1px solid rgba(255,255,255,0.1)", borderRadius:6, fontSize:11, cursor:"pointer", fontFamily:"inherit", fontWeight:600 }}>
            Submit
          </button>
        </div>
      </div>

      {/* Nav panel */}
      {showNav && (
        <div style={{ position:"fixed", top:50, right:12, zIndex:20, background:"rgba(18,32,64,0.98)", border:"1px solid rgba(255,255,255,0.1)", borderRadius:12, padding:16, width:280, maxHeight:"80vh", overflowY:"auto", backdropFilter:"blur(12px)" }}>
          <div style={{ fontSize:11, color:"#8B9DC3", letterSpacing:2, marginBottom:10, textTransform:"uppercase" }}>Questions</div>
          <div style={{ display:"grid", gridTemplateColumns:"repeat(6, 1fr)", gap:6 }}>
            {QUESTIONS.map((_, i) => (
              <button key={i} onClick={() => { setCurrent(i); setShowNav(false); }}
                style={{
                  width:36, height:36, borderRadius:6, border: i === current ? "2px solid #00979D" : "1px solid rgba(255,255,255,0.1)",
                  background: answers[i] !== undefined ? (flagged.has(i) ? "rgba(232,145,58,0.2)" : "rgba(0,151,157,0.15)") : "rgba(255,255,255,0.03)",
                  color: answers[i] !== undefined ? "#C0CAD8" : "#556B8A", fontSize:12, fontWeight:600, cursor:"pointer", fontFamily:"inherit",
                  display:"flex", alignItems:"center", justifyContent:"center"
                }}>
                {flagged.has(i) ? "⚑" : i + 1}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Question */}
      <div style={{ maxWidth:640, margin:"0 auto", padding:"32px 20px 100px" }}>
        <div style={{ display:"flex", justifyContent:"space-between", alignItems:"center", marginBottom:20 }}>
          <div>
            <span style={{ display:"inline-block", padding:"3px 10px", borderRadius:4, fontSize:10.5, fontWeight:600, letterSpacing:1, background:`${CAT_COLORS[q.cat]}22`, color:CAT_COLORS[q.cat], border:`1px solid ${CAT_COLORS[q.cat]}44`, textTransform:"uppercase" }}>
              {q.cat}
            </span>
          </div>
          <button onClick={() => toggleFlag(current)}
            style={{ padding:"4px 10px", background: flagged.has(current) ? "rgba(232,145,58,0.15)" : "transparent", border: flagged.has(current) ? "1px solid rgba(232,145,58,0.3)" : "1px solid rgba(255,255,255,0.1)", borderRadius:6, color: flagged.has(current) ? "#E8913A" : "#556B8A", fontSize:11, cursor:"pointer", fontFamily:"inherit" }}>
            {flagged.has(current) ? "⚑ Flagged" : "⚐ Flag"}
          </button>
        </div>

        <div style={{ fontSize:13, color:"#556B8A", marginBottom:6 }}>Question {current + 1} of {QUESTIONS.length}</div>
        <div style={{ fontSize:17, fontWeight:600, lineHeight:1.6, marginBottom:28, color:"#E8E6E3" }}>{q.q}</div>

        <div style={{ display:"flex", flexDirection:"column", gap:10 }}>
          {q.opts.map((opt, oi) => {
            const selected = answers[current] === oi;
            return (
              <button key={oi} onClick={() => select(current, oi)}
                style={{
                  padding:"14px 16px", borderRadius:10, border: selected ? "2px solid #00979D" : "1px solid rgba(255,255,255,0.08)",
                  background: selected ? "rgba(0,151,157,0.12)" : "rgba(255,255,255,0.03)",
                  color: selected ? "#E8E6E3" : "#C0CAD8", textAlign:"left", cursor:"pointer", fontFamily:"inherit", fontSize:14,
                  display:"flex", alignItems:"center", gap:12, transition:"all 0.15s"
                }}>
                <span style={{ width:28, height:28, borderRadius:6, display:"flex", alignItems:"center", justifyContent:"center", fontSize:12, fontWeight:700, background: selected ? "#00979D" : "rgba(255,255,255,0.06)", color: selected ? "#fff" : "#8B9DC3", flexShrink:0 }}>
                  {letters[oi]}
                </span>
                {opt}
              </button>
            );
          })}
        </div>

        <div style={{ fontSize:10.5, color:"#3D516F", marginTop:20, fontStyle:"italic" }}>{q.std}</div>

        {/* Bottom nav */}
        <div style={{ display:"flex", justifyContent:"space-between", marginTop:36 }}>
          <button onClick={() => setCurrent(Math.max(0, current - 1))} disabled={current === 0}
            style={{ padding:"10px 24px", background:"rgba(255,255,255,0.04)", color: current === 0 ? "#334" : "#8B9DC3", border:"1px solid rgba(255,255,255,0.08)", borderRadius:8, fontSize:12, cursor: current === 0 ? "default" : "pointer", fontFamily:"inherit" }}>
            ← Previous
          </button>
          <button onClick={() => setCurrent(Math.min(QUESTIONS.length - 1, current + 1))} disabled={current === QUESTIONS.length - 1}
            style={{ padding:"10px 24px", background: current < QUESTIONS.length - 1 ? "#00979D" : "rgba(255,255,255,0.04)", color: current < QUESTIONS.length - 1 ? "#fff" : "#334", border:"none", borderRadius:8, fontSize:12, cursor: current < QUESTIONS.length - 1 ? "pointer" : "default", fontFamily:"inherit", fontWeight:600 }}>
            Next →
          </button>
        </div>

        {/* Progress dots */}
        <div style={{ display:"flex", justifyContent:"center", gap:3, marginTop:24, flexWrap:"wrap" }}>
          {QUESTIONS.map((_, i) => (
            <div key={i} onClick={() => setCurrent(i)}
              style={{
                width: i === current ? 16 : 8, height:8, borderRadius:4, cursor:"pointer", transition:"all 0.2s",
                background: i === current ? "#00979D" : answers[i] !== undefined ? "rgba(0,151,157,0.4)" : "rgba(255,255,255,0.08)"
              }}/>
          ))}
        </div>
      </div>

      <style>{`
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 3px; }
      `}</style>
    </div>
  );
}
