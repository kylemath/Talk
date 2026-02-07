// Attentional Blink Interactive Website - Main JavaScript

// ===== TAB NAVIGATION =====
document.addEventListener('DOMContentLoaded', function() {
    // Tab switching
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabId = button.getAttribute('data-tab');
            
            // Remove active class from all tabs and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked tab and corresponding content
            button.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Initialize all charts
    initializeCharts();
    
    // Initialize demo
    initializeDemo();
});

// ===== CHART CONFIGURATIONS =====
const chartColors = {
    primary: '#667eea',
    secondary: '#764ba2',
    accent: '#f093fb',
    success: '#4ade80',
    danger: '#f87171',
    warning: '#fbbf24',
    background: 'rgba(102, 126, 234, 0.1)',
    grid: '#475569'
};

const commonChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            labels: {
                color: '#f1f5f9',
                font: { size: 14 }
            }
        }
    },
    scales: {
        x: {
            ticks: { color: '#cbd5e1' },
            grid: { color: chartColors.grid }
        },
        y: {
            ticks: { color: '#cbd5e1' },
            grid: { color: chartColors.grid }
        }
    }
};

let charts = {};

// ===== TAB 1: INTRODUCTION - AB CURVE =====
function createABCurveChart(blinkDepth = 0.5) {
    const ctx = document.getElementById('abCurveChart');
    if (!ctx) return;
    
    const lags = [1, 2, 3, 4, 5, 6, 7, 8];
    const accuracy = lags.map(lag => {
        if (lag === 1) return 85 + Math.random() * 5; // Lag-1 sparing
        if (lag >= 2 && lag <= 4) return 50 - (blinkDepth * 40) + Math.random() * 5; // Blink depth
        return 80 + (lag - 5) * 3 + Math.random() * 5; // Recovery
    });
    
    if (charts.abCurve) charts.abCurve.destroy();
    
    charts.abCurve = new Chart(ctx, {
        type: 'line',
        data: {
            labels: lags.map(l => `Lag ${l}`),
            datasets: [{
                label: 'T2 Accuracy (%)',
                data: accuracy,
                borderColor: chartColors.primary,
                backgroundColor: chartColors.background,
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointRadius: 6,
                pointHoverRadius: 8,
                pointBackgroundColor: chartColors.accent
            }]
        },
        options: {
            ...commonChartOptions,
            plugins: {
                ...commonChartOptions.plugins,
                title: {
                    display: true,
                    text: 'T2 Detection Accuracy vs T1-T2 Lag',
                    color: '#f1f5f9',
                    font: { size: 16 }
                }
            },
            scales: {
                ...commonChartOptions.scales,
                y: {
                    ...commonChartOptions.scales.y,
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: 'T2 Accuracy (%)',
                        color: '#cbd5e1'
                    }
                },
                x: {
                    ...commonChartOptions.scales.x,
                    title: {
                        display: true,
                        text: 'T1-T2 Lag',
                        color: '#cbd5e1'
                    }
                }
            }
        }
    });
}

// Blink depth slider
document.addEventListener('DOMContentLoaded', function() {
    const blinkDepthSlider = document.getElementById('blinkDepth');
    const blinkDepthValue = document.getElementById('blinkDepthValue');
    
    if (blinkDepthSlider) {
        blinkDepthSlider.addEventListener('input', function() {
            const value = parseFloat(this.value);
            blinkDepthValue.textContent = Math.round(value * 100) + '%';
            createABCurveChart(value);
        });
    }
});

// ===== TAB 2: TEMPORAL SELECTION - INDIVIDUAL DIFFERENCES =====
function createIndividualDiffChart(wmCapacity = 3, attentionFocus = 3) {
    const ctx = document.getElementById('individualDiffChart');
    if (!ctx) return;
    
    const lags = [1, 2, 3, 4, 5, 6, 7, 8];
    
    // Baseline AB curve
    const baselineAcc = lags.map(lag => {
        if (lag === 1) return 85;
        if (lag >= 2 && lag <= 4) return 45 + lag * 2;
        return 75 + (lag - 5) * 3;
    });
    
    // Individual performance based on WM and attention
    const performanceFactor = (wmCapacity + attentionFocus) / 10;
    const individualAcc = baselineAcc.map((acc, i) => {
        const improvement = (acc < 70) ? performanceFactor * 25 : performanceFactor * 10;
        return Math.min(95, acc + improvement);
    });
    
    if (charts.individualDiff) charts.individualDiff.destroy();
    
    charts.individualDiff = new Chart(ctx, {
        type: 'line',
        data: {
            labels: lags.map(l => `Lag ${l}`),
            datasets: [
                {
                    label: 'Average Performance',
                    data: baselineAcc,
                    borderColor: chartColors.grid,
                    backgroundColor: 'rgba(148, 163, 184, 0.1)',
                    borderWidth: 2,
                    borderDash: [5, 5],
                    fill: false,
                    tension: 0.4,
                    pointRadius: 4
                },
                {
                    label: 'Your Profile',
                    data: individualAcc,
                    borderColor: chartColors.accent,
                    backgroundColor: 'rgba(240, 147, 251, 0.2)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 6,
                    pointHoverRadius: 8
                }
            ]
        },
        options: {
            ...commonChartOptions,
            scales: {
                ...commonChartOptions.scales,
                y: {
                    ...commonChartOptions.scales.y,
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: 'T2 Accuracy (%)',
                        color: '#cbd5e1'
                    }
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const wmSlider = document.getElementById('wmCapacity');
    const wmValue = document.getElementById('wmValue');
    const focusSlider = document.getElementById('attentionFocus');
    const focusValue = document.getElementById('focusValue');
    
    if (wmSlider && focusSlider) {
        const updateChart = () => {
            const wm = parseFloat(wmSlider.value);
            const focus = parseFloat(focusSlider.value);
            wmValue.textContent = wm.toFixed(1);
            focusValue.textContent = focus.toFixed(1);
            createIndividualDiffChart(wm, focus);
        };
        
        wmSlider.addEventListener('input', updateChart);
        focusSlider.addEventListener('input', updateChart);
    }
});

// ===== TAB 3: NEURAL MECHANISMS - ERP TIMELINE =====
function createERPChart() {
    const ctx = document.getElementById('erpChart');
    if (!ctx) return;
    
    const timePoints = [];
    for (let t = 0; t <= 600; t += 10) {
        timePoints.push(t);
    }
    
    // P1 component (intact)
    const p1 = timePoints.map(t => {
        if (t >= 80 && t <= 120) return 5 * Math.sin((t - 80) * Math.PI / 40);
        return 0;
    });
    
    // N2pc component (disrupted during AB)
    const n2pc = timePoints.map(t => {
        if (t >= 180 && t <= 280) return -4 * Math.sin((t - 180) * Math.PI / 100);
        return 0;
    });
    
    // P3b component (absent during AB)
    const p3b = timePoints.map(t => {
        if (t >= 300 && t <= 500) return 6 * Math.sin((t - 300) * Math.PI / 200);
        return 0;
    });
    
    if (charts.erp) charts.erp.destroy();
    
    charts.erp = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timePoints,
            datasets: [
                {
                    label: 'P1 (Intact)',
                    data: p1,
                    borderColor: chartColors.success,
                    borderWidth: 2,
                    fill: false,
                    tension: 0.4,
                    pointRadius: 0
                },
                {
                    label: 'N2pc (Disrupted)',
                    data: n2pc,
                    borderColor: chartColors.danger,
                    borderWidth: 2,
                    fill: false,
                    tension: 0.4,
                    pointRadius: 0
                },
                {
                    label: 'P3b (Absent in AB)',
                    data: p3b,
                    borderColor: chartColors.warning,
                    borderWidth: 2,
                    fill: false,
                    tension: 0.4,
                    pointRadius: 0
                }
            ]
        },
        options: {
            ...commonChartOptions,
            scales: {
                ...commonChartOptions.scales,
                x: {
                    ...commonChartOptions.scales.x,
                    title: {
                        display: true,
                        text: 'Time (ms)',
                        color: '#cbd5e1'
                    },
                    ticks: {
                        ...commonChartOptions.scales.x.ticks,
                        stepSize: 100
                    }
                },
                y: {
                    ...commonChartOptions.scales.y,
                    title: {
                        display: true,
                        text: 'Amplitude (μV)',
                        color: '#cbd5e1'
                    }
                }
            }
        }
    });
}

// Feature Selectivity Chart
function createFeatureSelectivityChart(state = 'detected') {
    const ctx = document.getElementById('featureSelectivityChart');
    if (!ctx) return;
    
    const timePoints = Array.from({length: 61}, (_, i) => i * 10);
    
    let selectivity;
    if (state === 'detected') {
        selectivity = timePoints.map(t => {
            if (t < 100) return 0;
            if (t >= 100 && t <= 300) return (t - 100) / 200 * 0.8;
            return 0.8 + 0.2 * Math.sin((t - 300) / 50);
        });
    } else if (state === 'missed') {
        selectivity = timePoints.map(t => {
            if (t < 100) return 0;
            if (t >= 100 && t <= 200) return (t - 100) / 200 * 0.3;
            return 0.3 - 0.5 * Math.min((t - 200) / 200, 1);
        });
    } else { // distractor
        selectivity = timePoints.map(t => 0.1 + Math.random() * 0.05);
    }
    
    if (charts.featureSelectivity) charts.featureSelectivity.destroy();
    
    charts.featureSelectivity = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timePoints,
            datasets: [{
                label: `Neural Selectivity (${state})`,
                data: selectivity,
                borderColor: state === 'detected' ? chartColors.success : 
                            state === 'missed' ? chartColors.danger : chartColors.grid,
                backgroundColor: state === 'detected' ? 'rgba(74, 222, 128, 0.2)' :
                               state === 'missed' ? 'rgba(248, 113, 113, 0.2)' : 
                               'rgba(148, 163, 184, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointRadius: 0
            }]
        },
        options: {
            ...commonChartOptions,
            scales: {
                ...commonChartOptions.scales,
                x: {
                    ...commonChartOptions.scales.x,
                    title: { display: true, text: 'Time (ms)', color: '#cbd5e1' }
                },
                y: {
                    ...commonChartOptions.scales.y,
                    min: -0.5,
                    max: 1.2,
                    title: { display: true, text: 'Selectivity Index', color: '#cbd5e1' }
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const detectionStateSelect = document.getElementById('detectionState');
    if (detectionStateSelect) {
        detectionStateSelect.addEventListener('change', function() {
            createFeatureSelectivityChart(this.value);
        });
    }
});

// ===== TAB 4: DISCRETE VS CONTINUOUS - DUAL PROCESS =====
function createDualProcessChart(ampRate = 1.5, threshold = 0.6) {
    const ctx = document.getElementById('dualProcessChart');
    if (!ctx) return;
    
    const timePoints = Array.from({length: 61}, (_, i) => i * 10);
    
    // Item 1 (T1)
    const item1Continuous = timePoints.map(t => {
        if (t < 50) return 0.1;
        if (t >= 50 && t <= 150) return 0.1 * Math.exp(ampRate * (t - 50) / 100);
        return 0.1 * Math.exp(ampRate);
    });
    
    const item1Discrete = item1Continuous.map((val, i) => {
        if (timePoints[i] >= 350) return val > threshold ? 1 : 0;
        return null;
    });
    
    // Item 2 (T2 at ~300ms lag)
    const item2Continuous = timePoints.map(t => {
        if (t < 350) return 0.1;
        if (t >= 350 && t <= 450) return 0.1 * Math.exp(ampRate * (t - 350) / 100);
        return 0.1 * Math.exp(ampRate);
    });
    
    const item2Discrete = item2Continuous.map((val, i) => {
        if (timePoints[i] >= 450) return val > threshold ? 1 : 0;
        return null;
    });
    
    if (charts.dualProcess) charts.dualProcess.destroy();
    
    charts.dualProcess = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timePoints,
            datasets: [
                {
                    label: 'T1 Continuous Amplification',
                    data: item1Continuous,
                    borderColor: chartColors.primary,
                    borderWidth: 2,
                    fill: false,
                    tension: 0.3,
                    pointRadius: 0
                },
                {
                    label: 'T1 Discrete Selection',
                    data: item1Discrete,
                    borderColor: chartColors.accent,
                    borderWidth: 3,
                    fill: false,
                    tension: 0,
                    pointRadius: 5,
                    showLine: false
                },
                {
                    label: 'T2 Continuous Amplification',
                    data: item2Continuous,
                    borderColor: chartColors.secondary,
                    borderWidth: 2,
                    borderDash: [5, 5],
                    fill: false,
                    tension: 0.3,
                    pointRadius: 0
                },
                {
                    label: 'T2 Discrete Selection',
                    data: item2Discrete,
                    borderColor: chartColors.warning,
                    borderWidth: 3,
                    fill: false,
                    tension: 0,
                    pointRadius: 5,
                    showLine: false
                }
            ]
        },
        options: {
            ...commonChartOptions,
            scales: {
                ...commonChartOptions.scales,
                x: {
                    ...commonChartOptions.scales.x,
                    title: { display: true, text: 'Time (ms)', color: '#cbd5e1' }
                },
                y: {
                    ...commonChartOptions.scales.y,
                    min: 0,
                    max: 1.2,
                    title: { display: true, text: 'Activation Level', color: '#cbd5e1' }
                }
            },
            plugins: {
                ...commonChartOptions.plugins,
                annotation: {
                    annotations: {
                        thresholdLine: {
                            type: 'line',
                            yMin: threshold,
                            yMax: threshold,
                            borderColor: chartColors.danger,
                            borderWidth: 2,
                            borderDash: [10, 5],
                            label: {
                                content: 'Selection Threshold',
                                enabled: true,
                                position: 'end'
                            }
                        }
                    }
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const ampRateSlider = document.getElementById('ampRate');
    const ampValue = document.getElementById('ampValue');
    const thresholdSlider = document.getElementById('threshold');
    const threshValue = document.getElementById('threshValue');
    
    if (ampRateSlider && thresholdSlider) {
        const updateChart = () => {
            const amp = parseFloat(ampRateSlider.value);
            const thresh = parseFloat(thresholdSlider.value);
            ampValue.textContent = amp.toFixed(1);
            threshValue.textContent = thresh.toFixed(2);
            createDualProcessChart(amp, thresh);
        };
        
        ampRateSlider.addEventListener('input', updateChart);
        thresholdSlider.addEventListener('input', updateChart);
    }
});

// ===== TAB 5: MODELS - BLASTER AND SDT =====
function createBlasterChart(amplitude = 1, duration = 150, soa = 300) {
    const ctx = document.getElementById('blasterChart');
    if (!ctx) return;
    
    const timePoints = Array.from({length: 101}, (_, i) => i * 10);
    const sigma = duration / 2.355; // Convert FWHM to sigma
    
    // T1 blaster
    const t1Blaster = timePoints.map(t => {
        const t0 = 100;
        return amplitude * Math.exp(-Math.pow(t - t0, 2) / (2 * Math.pow(sigma, 2)));
    });
    
    // T2 blaster
    const t2Blaster = timePoints.map(t => {
        const t0 = 100 + soa;
        if (t0 > 1000) return 0;
        return amplitude * Math.exp(-Math.pow(t - t0, 2) / (2 * Math.pow(sigma, 2)));
    });
    
    // Detection threshold
    const detectionThreshold = timePoints.map(() => 0.3);
    
    if (charts.blaster) charts.blaster.destroy();
    
    charts.blaster = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timePoints,
            datasets: [
                {
                    label: 'T1 Blaster',
                    data: t1Blaster,
                    borderColor: chartColors.primary,
                    backgroundColor: 'rgba(102, 126, 234, 0.2)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                },
                {
                    label: 'T2 Blaster',
                    data: t2Blaster,
                    borderColor: chartColors.accent,
                    backgroundColor: 'rgba(240, 147, 251, 0.2)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                },
                {
                    label: 'Detection Threshold',
                    data: detectionThreshold,
                    borderColor: chartColors.danger,
                    borderWidth: 2,
                    borderDash: [10, 5],
                    fill: false,
                    pointRadius: 0
                }
            ]
        },
        options: {
            ...commonChartOptions,
            scales: {
                ...commonChartOptions.scales,
                x: {
                    ...commonChartOptions.scales.x,
                    title: { display: true, text: 'Time (ms)', color: '#cbd5e1' }
                },
                y: {
                    ...commonChartOptions.scales.y,
                    min: 0,
                    max: 2,
                    title: { display: true, text: 'Attentional Enhancement', color: '#cbd5e1' }
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const blasterAmpSlider = document.getElementById('blasterAmp');
    const blasterAmpValue = document.getElementById('blasterAmpValue');
    const blasterDurSlider = document.getElementById('blasterDuration');
    const blasterDurValue = document.getElementById('blasterDurValue');
    const soaSlider = document.getElementById('soa');
    const soaValue = document.getElementById('soaValue');
    
    if (blasterAmpSlider && blasterDurSlider && soaSlider) {
        const updateChart = () => {
            const amp = parseFloat(blasterAmpSlider.value);
            const dur = parseFloat(blasterDurSlider.value);
            const soa = parseFloat(soaSlider.value);
            blasterAmpValue.textContent = amp.toFixed(1);
            blasterDurValue.textContent = dur + ' ms';
            soaValue.textContent = soa + ' ms';
            createBlasterChart(amp, dur, soa);
        };
        
        blasterAmpSlider.addEventListener('input', updateChart);
        blasterDurSlider.addEventListener('input', updateChart);
        soaSlider.addEventListener('input', updateChart);
    }
});

// Signal Detection Theory Chart
function createSDTChart(dPrime = 2, criterion = 0) {
    const ctx = document.getElementById('sdtChart');
    if (!ctx) return;
    
    const xValues = [];
    for (let x = -4; x <= 6; x += 0.1) {
        xValues.push(x);
    }
    
    // Noise distribution (centered at 0)
    const noiseDistribution = xValues.map(x => 
        Math.exp(-0.5 * Math.pow(x, 2)) / Math.sqrt(2 * Math.PI)
    );
    
    // Signal distribution (centered at d')
    const signalDistribution = xValues.map(x => 
        Math.exp(-0.5 * Math.pow(x - dPrime, 2)) / Math.sqrt(2 * Math.PI)
    );
    
    if (charts.sdt) charts.sdt.destroy();
    
    charts.sdt = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xValues,
            datasets: [
                {
                    label: 'Noise (Non-Target)',
                    data: noiseDistribution,
                    borderColor: chartColors.grid,
                    backgroundColor: 'rgba(148, 163, 184, 0.2)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                },
                {
                    label: 'Signal (Target)',
                    data: signalDistribution,
                    borderColor: chartColors.success,
                    backgroundColor: 'rgba(74, 222, 128, 0.2)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                }
            ]
        },
        options: {
            ...commonChartOptions,
            scales: {
                ...commonChartOptions.scales,
                x: {
                    ...commonChartOptions.scales.x,
                    title: { display: true, text: 'Decision Variable', color: '#cbd5e1' },
                    ticks: {
                        callback: function(value, index) {
                            return index % 20 === 0 ? value.toFixed(1) : '';
                        },
                        color: '#cbd5e1'
                    }
                },
                y: {
                    ...commonChartOptions.scales.y,
                    title: { display: true, text: 'Probability Density', color: '#cbd5e1' }
                }
            },
            plugins: {
                ...commonChartOptions.plugins,
                tooltip: {
                    callbacks: {
                        title: function(context) {
                            return 'x = ' + xValues[context[0].dataIndex].toFixed(2);
                        }
                    }
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const sensitivitySlider = document.getElementById('sensitivity');
    const sensValue = document.getElementById('sensValue');
    const criterionSlider = document.getElementById('criterion');
    const critValue = document.getElementById('critValue');
    
    if (sensitivitySlider && criterionSlider) {
        const updateChart = () => {
            const sens = parseFloat(sensitivitySlider.value);
            const crit = parseFloat(criterionSlider.value);
            sensValue.textContent = sens.toFixed(1);
            critValue.textContent = crit.toFixed(1);
            createSDTChart(sens, crit);
        };
        
        sensitivitySlider.addEventListener('input', updateChart);
        criterionSlider.addEventListener('input', updateChart);
    }
});

// ===== TAB 6: INTERACTIVE DEMO =====
let demoState = {
    isRunning: false,
    sequence: [],
    t1: null,
    t2: null,
    t1Position: 0,
    t2Position: 0,
    userResponse: [],
    trials: []
};

function initializeDemo() {
    const startButton = document.getElementById('startDemo');
    const submitButton = document.getElementById('submitResponse');
    const resetButton = document.getElementById('resetDemo');
    const rateSlider = document.getElementById('demoRate');
    const rateValue = document.getElementById('demoRateValue');
    const lagSlider = document.getElementById('demoLag');
    const lagValue = document.getElementById('demoLagValue');
    
    if (rateSlider) {
        rateSlider.addEventListener('input', function() {
            rateValue.textContent = this.value + ' ms/item';
        });
    }
    
    if (lagSlider) {
        lagSlider.addEventListener('input', function() {
            lagValue.textContent = this.value;
        });
    }
    
    if (startButton) {
        startButton.addEventListener('click', startDemo);
    }
    
    if (submitButton) {
        submitButton.addEventListener('click', submitResponse);
    }
    
    if (resetButton) {
        resetButton.addEventListener('click', resetDemo);
    }
}

function startDemo() {
    const rate = parseInt(document.getElementById('demoRate').value);
    const lag = parseInt(document.getElementById('demoLag').value);
    
    // Hide results, show display
    document.getElementById('demoResults').style.display = 'none';
    document.getElementById('demoResponse').style.display = 'none';
    document.getElementById('demoDisplay').style.display = 'flex';
    
    // Generate sequence
    const letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'.split('');
    const sequence = [];
    const sequenceLength = 15;
    
    // Pick random positions for T1 and T2
    demoState.t1Position = 5 + Math.floor(Math.random() * 3); // Position 5-7
    demoState.t2Position = demoState.t1Position + lag;
    
    // Pick targets
    demoState.t1 = letters[Math.floor(Math.random() * letters.length)];
    let t2Options = letters.filter(l => l !== demoState.t1);
    demoState.t2 = t2Options[Math.floor(Math.random() * t2Options.length)];
    
    // Build sequence
    for (let i = 0; i < sequenceLength; i++) {
        if (i === demoState.t1Position) {
            sequence.push({ letter: demoState.t1, isTarget: true });
        } else if (i === demoState.t2Position) {
            sequence.push({ letter: demoState.t2, isTarget: true });
        } else {
            let distractor;
            do {
                distractor = letters[Math.floor(Math.random() * letters.length)];
            } while (distractor === demoState.t1 || distractor === demoState.t2 || 
                     (i > 0 && sequence[i-1].letter === distractor));
            sequence.push({ letter: distractor, isTarget: false });
        }
    }
    
    demoState.sequence = sequence;
    demoState.userResponse = [];
    
    // Run sequence
    runSequence(sequence, rate);
}

function runSequence(sequence, rate) {
    const letterElement = document.getElementById('demoLetter');
    let index = 0;
    
    const interval = setInterval(() => {
        if (index >= sequence.length) {
            clearInterval(interval);
            letterElement.textContent = '';
            showResponse();
            return;
        }
        
        const item = sequence[index];
        letterElement.textContent = item.letter;
        letterElement.style.color = item.isTarget ? '#667eea' : '#f1f5f9';
        
        index++;
    }, rate);
}

function showResponse() {
    document.getElementById('demoDisplay').style.display = 'none';
    const responseDiv = document.getElementById('demoResponse');
    responseDiv.style.display = 'block';
    
    // Create response options
    const optionsDiv = document.getElementById('responseOptions');
    optionsDiv.innerHTML = '';
    
    const allLetters = Array.from(new Set(demoState.sequence.map(s => s.letter)));
    allLetters.sort();
    
    allLetters.forEach(letter => {
        const option = document.createElement('div');
        option.className = 'response-option';
        option.textContent = letter;
        option.addEventListener('click', function() {
            this.classList.toggle('selected');
        });
        optionsDiv.appendChild(option);
    });
}

function submitResponse() {
    const selectedOptions = document.querySelectorAll('.response-option.selected');
    demoState.userResponse = Array.from(selectedOptions).map(el => el.textContent);
    
    // Calculate accuracy
    const detectedT1 = demoState.userResponse.includes(demoState.t1);
    const detectedT2 = demoState.userResponse.includes(demoState.t2);
    const lag = demoState.t2Position - demoState.t1Position;
    
    // Store trial
    demoState.trials.push({
        lag: lag,
        detectedT1: detectedT1,
        detectedT2: detectedT2
    });
    
    // Show results
    showResults(detectedT1, detectedT2, lag);
}

function showResults(detectedT1, detectedT2, lag) {
    document.getElementById('demoResponse').style.display = 'none';
    const resultsDiv = document.getElementById('demoResults');
    resultsDiv.style.display = 'block';
    
    const resultsContent = document.getElementById('resultsContent');
    
    let message = '';
    if (detectedT1 && detectedT2) {
        message = `<div style="color: #4ade80; font-size: 1.3em; margin-bottom: 1rem;">✓ Perfect! You detected both targets.</div>`;
        message += `<p>At lag ${lag}, you successfully overcame the attentional blink!</p>`;
    } else if (detectedT1 && !detectedT2) {
        message = `<div style="color: #fbbf24; font-size: 1.3em; margin-bottom: 1rem;">⚠ You experienced the attentional blink!</div>`;
        message += `<p>You detected T1 (<strong>${demoState.t1}</strong>) but missed T2 (<strong>${demoState.t2}</strong>).</p>`;
        message += `<p>At lag ${lag} (~${lag * 100}ms), your attention was still processing the first target.</p>`;
    } else if (!detectedT1 && detectedT2) {
        message = `<div style="color: #667eea; font-size: 1.3em; margin-bottom: 1rem;">⚡ Interesting!</div>`;
        message += `<p>You missed T1 (<strong>${demoState.t1}</strong>) but detected T2 (<strong>${demoState.t2}</strong>).</p>`;
        message += `<p>This sometimes happens when attention isn't engaged by T1.</p>`;
    } else {
        message = `<div style="color: #f87171; font-size: 1.3em; margin-bottom: 1rem;">✗ You missed both targets.</div>`;
        message += `<p>T1 was <strong>${demoState.t1}</strong> and T2 was <strong>${demoState.t2}</strong>.</p>`;
        message += `<p>The rapid presentation made it very challenging!</p>`;
    }
    
    resultsContent.innerHTML = message;
    
    // Update performance chart
    updatePerformanceChart();
}

function updatePerformanceChart() {
    const ctx = document.getElementById('performanceChart');
    if (!ctx) return;
    
    // Typical AB curve
    const lags = [1, 2, 3, 4, 5, 6, 7, 8];
    const typicalAcc = lags.map(lag => {
        if (lag === 1) return 85;
        if (lag >= 2 && lag <= 4) return 45 + lag * 5;
        return 75 + (lag - 5) * 5;
    });
    
    // User performance
    const userAcc = lags.map(lag => {
        const trialsAtLag = demoState.trials.filter(t => t.lag === lag);
        if (trialsAtLag.length === 0) return null;
        const correctTrials = trialsAtLag.filter(t => t.detectedT2 && t.detectedT1).length;
        return (correctTrials / trialsAtLag.length) * 100;
    });
    
    if (charts.performance) charts.performance.destroy();
    
    charts.performance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: lags.map(l => `Lag ${l}`),
            datasets: [
                {
                    label: 'Typical AB Curve',
                    data: typicalAcc,
                    borderColor: chartColors.grid,
                    borderWidth: 2,
                    borderDash: [5, 5],
                    fill: false,
                    tension: 0.4,
                    pointRadius: 4
                },
                {
                    label: 'Your Performance',
                    data: userAcc,
                    borderColor: chartColors.accent,
                    backgroundColor: 'rgba(240, 147, 251, 0.2)',
                    borderWidth: 3,
                    fill: false,
                    tension: 0.4,
                    pointRadius: 8,
                    pointHoverRadius: 10
                }
            ]
        },
        options: {
            ...commonChartOptions,
            scales: {
                ...commonChartOptions.scales,
                y: {
                    ...commonChartOptions.scales.y,
                    min: 0,
                    max: 100,
                    title: { display: true, text: 'Accuracy (%)', color: '#cbd5e1' }
                }
            }
        }
    });
}

function resetDemo() {
    document.getElementById('demoResults').style.display = 'none';
    document.getElementById('demoDisplay').style.display = 'flex';
    document.getElementById('demoLetter').textContent = '';
}

// ===== INITIALIZE ALL CHARTS =====
function initializeCharts() {
    // Tab 1: Introduction
    createABCurveChart(0.5);
    
    // Tab 2: Temporal Selection
    createIndividualDiffChart(3, 3);
    
    // Tab 3: Neural Mechanisms
    createERPChart();
    createFeatureSelectivityChart('detected');
    
    // Tab 4: Discrete vs Continuous
    createDualProcessChart(1.5, 0.6);
    
    // Tab 5: Theoretical Models
    createBlasterChart(1, 150, 300);
    createSDTChart(2, 0);
    
    // Tab 6: Interactive Demo
    // Performance chart created after trials
}

// MathJax configuration
window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
    },
    svg: {
        fontCache: 'global'
    }
};
