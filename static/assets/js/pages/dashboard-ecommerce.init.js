function getChartColorsArray(e) {
    if (null !== document.getElementById(e)) {
        var t = document.getElementById(e).getAttribute("data-colors");
        if (t)
            return (t = JSON.parse(t)).map(function(e) {
                var t = e.replace(" ", "");
                return -1 === t.indexOf(",") ? getComputedStyle(document.documentElement).getPropertyValue(t) || t : 2 == (e = e.split(",")).length ? "rgba(" + getComputedStyle(document.documentElement).getPropertyValue(e[0]) + "," + e[1] + ")" : t
            });
        console.warn("data-colors atributes not found on", e)
    }
}
var worldlinemap, overlay, options, chart, linechartcustomerColors = getChartColorsArray("customer_impression_charts"), chartDonutBasicColors = (linechartcustomerColors && (options = {
    series: [{
        name: "Milk",
        type: "area",
        data: weekly_data[2]
    }, {
        name: "Curd",
        type: "line",
        data: weekly_data[3]
    },
        {
            name: "Toned Milk",
            type: "line",
            data: weekly_data[4]
        }, {
            name: "Total",
            type: "bar",
            data: weekly_data[1]
        }],

    chart: {
        height: 310,
        type: "line",
        toolbar: {
            show: !1
        }
    },
    stroke: {
        curve: "straight",
        dashArray: [0, 0, 8],
        width: [.1, 0, 2]
    },
    fill: {
        opacity: [.03, .9, 1]
    },
    markers: {
        size: [0, 0, 0],
        strokeWidth: 2,
        hover: {
            size: 4
        }
    },
    xaxis: {
        categories: weekly_data[0],//["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        axisTicks: {
            show: !1
        },
        axisBorder: {
            show: !1
        }
    },
    grid: {
        show: !0,
        xaxis: {
            lines: {
                show: !0
            }
        },
        yaxis: {
            lines: {
                show: !1
            }
        },
        padding: {
            top: 0,
            right: -2,
            bottom: 15,
            left: 10
        }
    },
    legend: {
        show: !0,
        horizontalAlign: "center",
        offsetX: 0,
        offsetY: -5,
        markers: {
            width: 9,
            height: 9,
            radius: 6
        },
        itemMargin: {
            horizontal: 10,
            vertical: 0
        }
    },
    plotOptions: {
        bar: {
            columnWidth: "20%",
            barHeight: "100%",
            borderRadius: [8]
        }
    },
    colors: linechartcustomerColors,
    tooltip: {
        shared: !0,
        y: [{
            formatter: function(e) {
                return void 0 !== e ? e.toFixed(0) : e
            }
        }, {
            formatter: function(e) {
                return void 0 !== e ? e + " packets" : e
            }
        }, {
            formatter: function(e) {
                return void 0 !== e ? e.toFixed(0) + " packets" : e
            }
        },
            {
                formatter: function (e) {
                    return void 0 !== e ? e + " packets" : e
                }
            }]
    }
},
(chart = new ApexCharts(document.querySelector("#customer_impression_charts"),options)).render()),
getChartColorsArray("#store-visits-source")), vectorMapWorldLineColors = (chartDonutBasicColors && (options = {
    series: [44, 55, 41, 17, 15],
    labels: ["Direct", "Social", "Email", "Other", "Referrals"],
    chart: {
        height: 333,
        type: "donut"
    },
    legend: {
        position: "bottom"
    },
    stroke: {
        show: !1
    },
    dataLabels: {
        dropShadow: {
            enabled: !1
        }
    },
    colors: chartDonutBasicColors
},
(chart = new ApexCharts(document.querySelector("#store-visits-source"),options)).render()),
getChartColorsArray("world-map-line-markers")), layoutRightSideBtn = (vectorMapWorldLineColors && (worldlinemap = new jsVectorMap({
    map: "world_merc",
    selector: "#world-map-line-markers",
    zoomOnScroll: !1,
    zoomButtons: !1,
    markers: [{
        name: "Greenland",
        coords: [72, -42]
    }, {
        name: "Canada",
        coords: [56.1304, -106.3468]
    }, {
        name: "Brazil",
        coords: [-14.235, -51.9253]
    }, {
        name: "Serbia",
        coords: [44.0165, 21.0059]
    }, {
        name: "Russia",
        coords: [61, 105]
    }, {
        name: "China",
        coords: [35.8617, 104.1954]
    }, {
        name: "United States",
        coords: [37.0902, -95.7129]
    }, {
        name: "Norway",
        coords: [60.472024, 8.468946]
    }, {
        name: "Sydney",
        coords: [33.8688, 151.2093]
    }],
    lines: [{
        from: "Canada",
        to: "Serbia"
    }, {
        from: "Russia",
        to: "Serbia"
    }, {
        from: "Greenland",
        to: "Serbia"
    }, {
        from: "Brazil",
        to: "Serbia"
    }, {
        from: "United States",
        to: "Serbia"
    }, {
        from: "China",
        to: "Serbia"
    }, {
        from: "Norway",
        to: "Serbia"
    }, {
        from: "Sydney",
        to: "Serbia"
    }],
    regionStyle: {
        initial: {
            stroke: "#9599ad",
            strokeWidth: .25,
            fill: vectorMapWorldLineColors,
            fillOpacity: 1
        }
    },
    labels: {
        markers: {
            render(e, t) {
                return e.name || e.labelName || "Not available"
            }
        }
    },
    lineStyle: {
        animation: !0,
        strokeDasharray: "6 3 6"
    }
})),
document.querySelector(".layout-rightside-btn")), swiper = (layoutRightSideBtn && (Array.from(document.querySelectorAll(".layout-rightside-btn")).forEach(function(e) {
    var t = document.querySelector(".layout-rightside-col");
    e.addEventListener("click", function() {
        document.querySelectorAll(".layout-rightside").forEach(function(e) {
            e.classList.remove("show")
        }),
        t.classList.contains("d-block") ? (t.classList.remove("d-block"),
        t.classList.add("d-none")) : (t.classList.remove("d-none"),
        t.classList.add("d-block"))
    })
}),
window.addEventListener("resize", function() {
    var e = document.querySelector(".layout-rightside-col");
    e && Array.from(document.querySelectorAll(".layout-rightside-btn")).forEach(function() {
        window.outerWidth < 1699 || 3440 < window.outerWidth ? e.classList.remove("d-block") : 1699 < window.outerWidth && e.classList.add("d-block")
    })
}),
overlay = document.querySelector(".overlay")) && document.querySelector(".overlay").addEventListener("click", function() {
    1 == document.querySelector(".layout-rightside-col").classList.contains("d-block") && document.querySelector(".layout-rightside-col").classList.remove("d-block")
}),
window.addEventListener("load", function() {
    var e = document.querySelector(".layout-rightside-col");
    e && Array.from(document.querySelectorAll(".layout-rightside-btn")).forEach(function() {
        window.outerWidth < 1699 || 3440 < window.outerWidth ? e.classList.remove("d-block") : 1699 < window.outerWidth && e.classList.add("d-block")
    })
}),
new Swiper(".selling-product",{
    slidesPerView: "auto",
    spaceBetween: 15,
    autoplay: {
        delay: 2500,
        disableOnInteraction: !1
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    }
})), chartRadialbarMultipleColors = getChartColorsArray("multiple_radialbar");
function currentTime() {
    var e = 12 <= (new Date).getHours() ? "pm" : "am"
      , t = 12 < (new Date).getHours() ? (new Date).getHours() % 12 : (new Date).getHours()
      , r = (new Date).getMinutes() < 10 ? "0" + (new Date).getMinutes() : (new Date).getMinutes();
    return t < 10 ? "0" + t + ":" + r + " " + e : t + ":" + r + " " + e
}
chartRadialbarMultipleColors && (options = {
    series: total_data[0],
    chart: {
        height: 350,
        type: "radialBar"
    },
    plotOptions: {
        radialBar: {
            dataLabels: {
                name: {
                    fontSize: "22px"
                },
                value: {
                    fontSize: "16px"
                },
                total: {
                    show: !0,
                    label: "Total",
                    formatter: function(e) {
                        return total_data[1]
                    }
                }
                
            }
        }
    },
    labels: ["Milk", "Curd", "Tonned Milk"],// "Others"],
    colors: chartRadialbarMultipleColors,
    legend: {
        show: !0,
        fontSize: "16px",
        position: "bottom",
        labels: {
            useSeriesColors: !0
        },
        markers: {
            size: 0
        }
    }
},
(chart = new ApexCharts(document.querySelector("#multiple_radialbar"),options)).render()),
document.querySelectorAll(".chat-panel-list li").forEach(function(r) {
    r.addEventListener("click", function() {
        document.querySelectorAll(".layout-rightside").forEach(function(e) {
            e.classList.add("show")
        });
        var e = r.querySelector(".chatlist-user-name").innerHTML
          , t = r.querySelector(".chatlist-user-image").getAttribute("src")
          , e = (document.querySelector(".chat-topbar .profile-username").innerHTML = e,
        document.querySelector(".chat-topbar .userprofile").setAttribute("src", t),
        document.getElementById("users-conversation"));
        Array.from(e.querySelectorAll(".left .chat-avatar")).forEach(function(e) {
            t ? e.querySelector("img").setAttribute("src", t) : e.querySelector("img").setAttribute("src", dummyUserImage)
        })
    })
})