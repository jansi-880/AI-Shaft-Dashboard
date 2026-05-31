# =========================================================
# AI BASED SHAFT DESIGN AND ANALYSIS DASHBOARD
# FULL WORKING CODE
# NO UTF ERROR
# NO SQRT ERROR
# PDF DOWNLOAD WORKING
# DIAGRAMS + FBD + CALCULATIONS IN PDF
# =========================================================

import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
import tempfile

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

st.set_page_config(page_title="AI Shaft Dashboard", layout="wide")

st.title("AI Based Shaft Design and Analysis Dashboard")

shaft = st.sidebar.selectbox(
    "Select Shaft Type",
    [
        "Solid Shaft",
        "Hollow Shaft",
        "Single Gear Shaft",
        "Gear + Pulley Shaft"
    ]
)
# =====================================================
# SOLID SHAFT
# =====================================================

if shaft == "Solid Shaft":

    st.header("Solid Shaft Design")

    power = st.number_input(
        "Power (kW)",
        value=None
    )

    speed = st.number_input(
        "Speed (RPM)",
        value=None
    )

    stress = st.number_input(
        "Allowable Shear Stress (MPa)",
        value=None
    )

    if st.button("Calculate Solid Shaft"):

        # CALCULATIONS

        T = (9550 * power * 1000) / speed

        d = ((16 * T) / (3.14 * stress)) ** (1/3)

        # RESULTS

        st.subheader("Results")

        st.write("Torque =", round(T,2), "N-mm")

        st.write("Diameter =", round(d,2), "mm")

        # =====================================================
        # ACTUAL SHAFT DIAGRAM
        # =====================================================

        st.subheader("Actual Shaft Diagram")

        fig1, ax1 = plt.subplots(figsize=(10,2))

        ax1.plot([0,10],[0,0], linewidth=18)

        ax1.text(4,-0.5,"Solid Shaft")

        ax1.axis("off")

        st.pyplot(fig1)

        # =====================================================
        # 3D SHAFT VIEW
        # =====================================================

        st.subheader("3D Shaft View")

        fig3d, ax3d = plt.subplots(figsize=(10,3))

        # Shaft body

        ax3d.fill(
            [1,9,9.5,1.5],
            [1,1,2,2],
            color='gray',
            alpha=0.7
        )

        # Front circle

        front = plt.Circle(
            (1.5,1.5),
            0.5,
            color='dimgray'
        )

        # Back circle

        back = plt.Circle(
            (9.5,1.5),
            0.5,
            color='lightgray'
        )

        ax3d.add_patch(front)

        ax3d.add_patch(back)

        ax3d.text(4,2.5,"3D Solid Shaft")

        ax3d.axis("off")

        st.pyplot(fig3d)

        # =====================================================
        # FREE BODY DIAGRAM
        # =====================================================

        st.subheader("Free Body Diagram")

        fig2, ax2 = plt.subplots(figsize=(10,3))

        ax2.plot([0,10],[0,0], linewidth=8)

        ax2.plot(0,0,'ks', markersize=12)

        ax2.plot(10,0,'ks', markersize=12)

        ax2.arrow(
            5,2,0,-1.5,
            head_width=0.3,
            head_length=0.2
        )

        ax2.text(5,2.2,"Torque")

        ax2.axis("off")

        st.pyplot(fig2)

        # =====================================================
        # STEP BY STEP SOLUTION
        # =====================================================

        st.subheader("Step By Step Analytical Solution")

        st.code(
            f"T = (9550 * {power} * 1000) / {speed}"
        )

        st.code(
            f"T = {round(T,2)} N-mm"
        )

        st.code(
            f"d = ((16 * {round(T,2)}) / "
            f"(3.14 * {stress}))^(1/3)"
        )

        st.code(
            f"d = {round(d,2)} mm"
        )

        st.code(
            "Formula Used:"
        )

        st.code(
            "T = (9550 * P * 1000) / N"
        )

        st.code(
            "d = ((16 * T) / (pi * tau))^(1/3)"
        )

        # =====================================================
        # PDF REPORT
        # =====================================================

        pdf_buffer = BytesIO()

        doc = SimpleDocTemplate(pdf_buffer)

        elements = []

        elements.append(
            Paragraph(
                "Solid Shaft Report",
                styles['Title']
            )
        )

        elements.append(Spacer(1,20))

        elements.append(
            Paragraph(
                f"Power = {power}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Speed = {speed}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Stress = {stress}",
                styles['BodyText']
            )
        )

        # =====================================================
        # SHAFT IMAGE
        # =====================================================

        temp1 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig1.savefig(temp1.name)

        elements.append(
            Image(
                temp1.name,
                width=400,
                height=120
            )
        )

        # =====================================================
        # 3D IMAGE
        # =====================================================

        temp3d = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig3d.savefig(temp3d.name)

        elements.append(
            Image(
                temp3d.name,
                width=400,
                height=150
            )
        )

        # =====================================================
        # FBD IMAGE
        # =====================================================

        temp2 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig2.savefig(temp2.name)

        elements.append(
            Image(
                temp2.name,
                width=400,
                height=120
            )
        )

        # =====================================================
        # PDF CALCULATIONS
        # =====================================================

        elements.append(
            Paragraph(
                "Step By Step Calculations",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                f"T = (9550 * {power} * 1000) / {speed}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"T = {round(T,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = ((16 * {round(T,2)}) / "
                f"(3.14 * {stress}))^(1/3)",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = {round(d,2)} mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "Formula Used:",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                "T = (9550 * P * 1000) / N",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "d = ((16 * T) / (pi * tau))^(1/3)",
                styles['BodyText']
            )
        )

        doc.build(elements)

        pdf_buffer.seek(0)

        st.download_button(
            "Download Full PDF Report",
            data=pdf_buffer,
            file_name="solid_shaft_report.pdf",
            mime="application/pdf"
        )
# =====================================================
# HOLLOW SHAFT
# =====================================================

elif shaft == "Hollow Shaft":

    st.header("Hollow Shaft Design")

    power = st.number_input(
        "Power (kW)",
        value=None
    )

    speed = st.number_input(
        "Speed (RPM)",
        value=None
    )

    stress = st.number_input(
        "Allowable Stress (MPa)",
        value=None
    )

    ratio = st.number_input(
        "d/D Ratio",
        value=None
    )

    if st.button("Calculate Hollow Shaft"):

        # =====================================================
        # CALCULATIONS
        # =====================================================

        T = (9550 * power * 1000) / speed

        D = (
            (16 * T) /
            (3.14 * stress * (1 - ratio**4))
        ) ** (1/3)

        d = ratio * D

        # =====================================================
        # RESULTS
        # =====================================================

        st.subheader("Results")

        st.write("Torque =", round(T,2), "N-mm")

        st.write("Outer Diameter =", round(D,2), "mm")

        st.write("Inner Diameter =", round(d,2), "mm")

        # =====================================================
        # ACTUAL SHAFT DIAGRAM
        # =====================================================

        st.subheader("Actual Hollow Shaft Diagram")

        fig3, ax3 = plt.subplots(figsize=(10,2))

        ax3.plot([0,10],[0,0], linewidth=18)

        ax3.plot(
            [0,10],
            [0,0],
            linewidth=8,
            color='white'
        )

        ax3.text(4,-0.5,"Hollow Shaft")

        ax3.axis("off")

        st.pyplot(fig3)

        # =====================================================
        # 3D HOLLOW SHAFT VIEW
        # =====================================================

        st.subheader("3D Hollow Shaft View")

        fig3d, ax3d = plt.subplots(figsize=(10,3))

        # Main body

        ax3d.fill(
            [1,9,9.5,1.5],
            [1,1,2,2],
            color='silver',
            alpha=0.8
        )

        # Front outer circle

        front_outer = plt.Circle(
            (1.5,1.5),
            0.5,
            color='gray'
        )

        # Front inner hole

        front_inner = plt.Circle(
            (1.5,1.5),
            0.2,
            color='white'
        )

        # Back outer circle

        back_outer = plt.Circle(
            (9.5,1.5),
            0.5,
            color='lightgray'
        )

        # Back inner hole

        back_inner = plt.Circle(
            (9.5,1.5),
            0.2,
            color='white'
        )

        ax3d.add_patch(front_outer)

        ax3d.add_patch(front_inner)

        ax3d.add_patch(back_outer)

        ax3d.add_patch(back_inner)

        ax3d.text(3.5,2.5,"3D Hollow Shaft")

        ax3d.axis("off")

        st.pyplot(fig3d)

        # =====================================================
        # SECTION VIEW
        # =====================================================

        st.subheader("Section View")

        fig4, ax4 = plt.subplots(figsize=(5,5))

        outer = plt.Circle(
            (0,0),
            5,
            fill=False,
            linewidth=5
        )

        inner = plt.Circle(
            (0,0),
            2.5,
            fill=False,
            linewidth=5
        )

        ax4.add_patch(outer)

        ax4.add_patch(inner)

        ax4.set_xlim(-6,6)

        ax4.set_ylim(-6,6)

        ax4.set_aspect("equal")

        ax4.axis("off")

        st.pyplot(fig4)

        # =====================================================
        # STEP BY STEP SOLUTION
        # =====================================================

        st.subheader("Step By Step Analytical Solution")

        st.code(
            f"T = (9550 * {power} * 1000) / {speed}"
        )

        st.code(
            f"T = {round(T,2)} N-mm"
        )

        st.code(
            f"D = ((16 * {round(T,2)}) / "
            f"(3.14 * {stress} * "
            f"(1 - {ratio}^4)))^(1/3)"
        )

        st.code(
            f"D = {round(D,2)} mm"
        )

        st.code(
            f"d = {ratio} * {round(D,2)}"
        )

        st.code(
            f"d = {round(d,2)} mm"
        )

        st.code(
            "Formula Used:"
        )

        st.code(
            "T = (9550 * P * 1000) / N"
        )

        st.code(
            "D = ((16 * T) / "
            "(pi * tau * (1-k^4)))^(1/3)"
        )

        st.code(
            "d = k * D"
        )

        # =====================================================
        # PDF REPORT
        # =====================================================

        pdf_buffer = BytesIO()

        doc = SimpleDocTemplate(pdf_buffer)

        elements = []

        elements.append(
            Paragraph(
                "Hollow Shaft Report",
                styles['Title']
            )
        )

        elements.append(Spacer(1,20))

        elements.append(
            Paragraph(
                f"Power = {power}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Speed = {speed}",
                styles['BodyText']
            )
        )	

        elements.append(
            Paragraph(
                f"Stress = {stress}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d/D Ratio = {ratio}",
                styles['BodyText']
            )
        )

        # =====================================================
        # SHAFT IMAGE
        # =====================================================

        temp3 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig3.savefig(temp3.name)

        elements.append(
            Image(
                temp3.name,
                width=400,
                height=120
            )
        )

        # =====================================================
        # 3D IMAGE
        # =====================================================

        temp3d = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig3d.savefig(temp3d.name)

        elements.append(
            Image(
                temp3d.name,
                width=400,
                height=150
            )
        )

        # =====================================================
        # SECTION VIEW IMAGE
        # =====================================================

        temp4 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig4.savefig(temp4.name)

        elements.append(
            Image(
                temp4.name,
                width=300,
                height=300
            )
        )

        # =====================================================
        # PDF CALCULATIONS
        # =====================================================

        elements.append(
            Paragraph(
                "Step By Step Calculations",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                f"T = (9550 * {power} * 1000) / {speed}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"T = {round(T,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"D = ((16 * {round(T,2)}) / "
                f"(3.14 * {stress} * "
                f"(1 - {ratio}^4)))^(1/3)",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"D = {round(D,2)} mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = {ratio} * {round(D,2)}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = {round(d,2)} mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "Formula Used:",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                "T = (9550 * P * 1000) / N",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "D = ((16 * T) / "
                "(pi * tau * (1-k^4)))^(1/3)",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "d = k * D",
                styles['BodyText']
            )
        )

        doc.build(elements)

        pdf_buffer.seek(0)

        st.download_button(
            "Download Full PDF Report",
            data=pdf_buffer,
            file_name="hollow_shaft_report.pdf",
            mime="application/pdf"
        )
# =====================================================
# SINGLE GEAR SHAFT
# =====================================================

elif shaft == "Single Gear Shaft":

    st.header("Single Gear Shaft")

    power = st.number_input(
        "Power (kW)",
        value=None
    )

    speed = st.number_input(
        "Speed (RPM)",
        value=None
    )

    gear_force = st.number_input(
        "Gear Force (N)",
        value=None
    )

    length = st.number_input(
        "Length (mm)",
        value=None
    )

    stress = st.number_input(
        "Allowable Stress (MPa)",
        value=None
    )

    if st.button("Calculate Single Gear Shaft"):

        # =====================================================
        # CALCULATIONS
        # =====================================================

        T = (9550 * power * 1000) / speed

        M = (gear_force * length) / 4

        Te = ((M**2) + (T**2)) ** 0.5

        d = ((16 * Te) / (3.14 * stress)) ** (1/3)

        # =====================================================
        # RESULTS
        # =====================================================

        st.subheader("Results")

        st.write("Torque =", round(T,2), "N-mm")

        st.write("Bending Moment =", round(M,2), "N-mm")

        st.write("Equivalent Torque =", round(Te,2), "N-mm")

        st.write("Diameter =", round(d,2), "mm")

        # =====================================================
        # ACTUAL SHAFT DIAGRAM
        # =====================================================

        st.subheader("Actual Shaft Diagram")

        fig5, ax5 = plt.subplots(figsize=(10,3))

        ax5.plot([0,length],[0,0], linewidth=10)

        gear = plt.Circle(
            (length/2,0),
            40,
            fill=False,
            linewidth=4
        )

        ax5.add_patch(gear)

        ax5.text(length/2,-80,"Gear")

        ax5.axis("off")

        st.pyplot(fig5)

        # =====================================================
        # 3D SHAFT VIEW
        # =====================================================

        st.subheader("3D Shaft View")

        fig3d, ax3d = plt.subplots(figsize=(10,3))

        # Shaft body

        ax3d.fill(
            [1,9,9.5,1.5],
            [1,1,2,2],
            color='gray',
            alpha=0.7
        )

        # Front circle

        front = plt.Circle(
            (1.5,1.5),
            0.5,
            color='dimgray'
        )

        # Back circle

        back = plt.Circle(
            (9.5,1.5),
            0.5,
            color='lightgray'
        )

        # Gear

        gear3d = plt.Circle(
            (5.5,1.5),
            0.8,
            fill=False,
            linewidth=4,
            color='black'
        )

        ax3d.add_patch(front)

        ax3d.add_patch(back)

        ax3d.add_patch(gear3d)

        ax3d.text(4,2.8,"3D Single Gear Shaft")

        ax3d.axis("off")

        st.pyplot(fig3d)

        # =====================================================
        # FREE BODY DIAGRAM
        # =====================================================

        st.subheader("Free Body Diagram")

        fig6, ax6 = plt.subplots(figsize=(10,3))

        ax6.plot([0,length],[0,0], linewidth=8)

        ax6.plot(0,0,'ks', markersize=12)

        ax6.plot(length,0,'ks', markersize=12)

        ax6.arrow(
            length/2,
            100,
            0,
            -80,
            head_width=20,
            head_length=20
        )

        ax6.text(length/2,110,"Gear Force")

        ax6.axis("off")

        st.pyplot(fig6)

        # =====================================================
        # STEP BY STEP ANALYTICAL SOLUTION
        # =====================================================

        st.subheader("Step By Step Analytical Solution")

        st.code(
            f"T = (9550 * {power} * 1000) / {speed}"
        )

        st.code(
            f"T = {round(T,2)} N-mm"
        )

        st.code(
            f"M = ({gear_force} * {length}) / 4"
        )

        st.code(
            f"M = {round(M,2)} N-mm"
        )

        st.code(
            f"Te = sqrt(({round(M,2)}^2) + ({round(T,2)}^2))"
        )

        st.code(
            f"Te = {round(Te,2)} N-mm"
        )

        st.code(
            f"d = ((16 * {round(Te,2)}) / "
            f"(3.14 * {stress}))^(1/3)"
        )

        st.code(
            f"d = {round(d,2)} mm"
        )

        st.code(
            "Formula Used:"
        )

        st.code(
            "T = (9550 * P * 1000) / N"
        )

        st.code(
            "M = (F * L) / 4"
        )

        st.code(
            "Te = sqrt(M^2 + T^2)"
        )

        st.code(
            "d = ((16 * Te) / (pi * tau))^(1/3)"
        )

        # =====================================================
        # PDF REPORT
        # =====================================================

        pdf_buffer = BytesIO()

        doc = SimpleDocTemplate(pdf_buffer)

        elements = []

        elements.append(
            Paragraph(
                "Single Gear Shaft Report",
                styles['Title']
            )
        )

        elements.append(Spacer(1,20))

        elements.append(
            Paragraph(
                f"Power = {power}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Speed = {speed}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Gear Force = {gear_force}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Length = {length}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Stress = {stress}",
                styles['BodyText']
            )
        )

        # =====================================================
        # SHAFT IMAGE
        # =====================================================

        temp5 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig5.savefig(temp5.name)

        elements.append(
            Image(
                temp5.name,
                width=400,
                height=120
            )
        )

        # =====================================================
        # 3D IMAGE
        # =====================================================

        temp3d = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig3d.savefig(temp3d.name)

        elements.append(
            Image(
                temp3d.name,
                width=400,
                height=150
            )
        )

        # =====================================================
        # FBD IMAGE
        # =====================================================

        temp6 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig6.savefig(temp6.name)

        elements.append(
            Image(
                temp6.name,
                width=400,
                height=120
            )
        )

        # =====================================================
        # PDF CALCULATIONS
        # =====================================================

        elements.append(
            Paragraph(
                "Step By Step Calculations",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                f"T = (9550 * {power} * 1000) / {speed}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"T = {round(T,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"M = ({gear_force} * {length}) / 4",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"M = {round(M,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Te = sqrt(({round(M,2)}^2) + ({round(T,2)}^2))",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Te = {round(Te,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = ((16 * {round(Te,2)}) / "
                f"(3.14 * {stress}))^(1/3)",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = {round(d,2)} mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "Formula Used:",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                "T = (9550 * P * 1000) / N",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "M = (F * L) / 4",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "Te = sqrt(M^2 + T^2)",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "d = ((16 * Te) / (pi * tau))^(1/3)",
                styles['BodyText']
            )
        )

        doc.build(elements)

        pdf_buffer.seek(0)

        st.download_button(
            "Download Full PDF Report",
            data=pdf_buffer,
            file_name="single_gear_shaft_report.pdf",
            mime="application/pdf"
        )
# =====================================================
# GEAR + PULLEY SHAFT
# =====================================================

elif shaft == "Gear + Pulley Shaft":

    st.header("Gear + Pulley Shaft Design")

    P = st.number_input(
        "Power (kW)",
        value=1.0
    )

    N = st.number_input(
        "Speed (RPM)",
        value=1440.0
    )

    Fg = st.number_input(
        "Gear Force (N)",
        value=1000.0
    )

    T1 = st.number_input(
        "Tight Side Tension T1 (N)",
        value=500.0
    )

    T2 = st.number_input(
        "Slack Side Tension T2 (N)",
        value=200.0
    )

    L = st.number_input(
        "Length (mm)",
        value=500.0
    )

    tau = st.number_input(
        "Stress (MPa)",
        value=40.0
    )

    if st.button("Calculate Gear + Pulley Shaft"):

        # =====================================================
        # CALCULATIONS
        # =====================================================

        Fp = T1 - T2

        T = (9550 * P * 1000) / N

        M = ((Fg + Fp) * L) / 4

        Te = ((M**2) + (T**2)) ** 0.5

        d = ((16 * Te) / (3.14 * tau)) ** (1/3)

        # =====================================================
        # RESULTS
        # =====================================================

        st.subheader("Results")

        st.write("Pulley Force =", round(Fp,2), "N")

        st.write("Torque =", round(T,2), "N-mm")

        st.write("Bending Moment =", round(M,2), "N-mm")

        st.write("Equivalent Torque =", round(Te,2), "N-mm")

        st.write("Diameter =", round(d,2), "mm")

        # =====================================================
        # ACTUAL SHAFT DIAGRAM
        # =====================================================

        st.subheader("Actual Shaft Diagram")

        fig7, ax7 = plt.subplots(figsize=(10,3))

        ax7.plot([0,L],[0,0], linewidth=8)

        gear_pos = L * 0.3

        pulley_pos = L * 0.7

        gear = plt.Circle(
            (gear_pos,0),
            30,
            fill=False,
            linewidth=3
        )

        pulley = plt.Circle(
            (pulley_pos,0),
            30,
            fill=False,
            linewidth=3
        )

        ax7.add_patch(gear)

        ax7.add_patch(pulley)

        ax7.text(gear_pos,-60,"Gear")

        ax7.text(pulley_pos,-60,"Pulley")

        ax7.axis("off")

        st.pyplot(fig7)

        # =====================================================
        # 3D SHAFT VIEW
        # =====================================================

        st.subheader("3D Shaft View")

        fig3d, ax3d = plt.subplots(figsize=(10,3))

        # Shaft body

        ax3d.fill(
            [1,9,9.5,1.5],
            [1,1,2,2],
            color='gray',
            alpha=0.7
        )

        # Front circle

        front = plt.Circle(
            (1.5,1.5),
            0.5,
            color='dimgray'
        )

        # Back circle

        back = plt.Circle(
            (9.5,1.5),
            0.5,
            color='lightgray'
        )

        # Gear

        gear3d = plt.Circle(
            (4,1.5),
            0.8,
            fill=False,
            linewidth=4,
            color='black'
        )

        # Pulley

        pulley3d = plt.Circle(
            (7,1.5),
            0.8,
            fill=False,
            linewidth=4,
            color='blue'
        )

        ax3d.add_patch(front)

        ax3d.add_patch(back)

        ax3d.add_patch(gear3d)

        ax3d.add_patch(pulley3d)

        ax3d.text(3,2.8,"3D Gear + Pulley Shaft")

        ax3d.axis("off")

        st.pyplot(fig3d)

        # =====================================================
        # FREE BODY DIAGRAM
        # =====================================================

        st.subheader("Free Body Diagram")

        fig8, ax8 = plt.subplots(figsize=(10,3))

        ax8.plot([0,L],[0,0], linewidth=6)

        ax8.arrow(
            gear_pos,
            120,
            0,
            -90,
            head_width=15,
            head_length=15
        )

        ax8.text(gear_pos,130,"Fg")

        ax8.arrow(
            pulley_pos - 10,
            120,
            0,
            -90,
            head_width=15,
            head_length=15
        )

        ax8.arrow(
            pulley_pos + 10,
            120,
            0,
            -90,
            head_width=15,
            head_length=15
        )

        ax8.text(pulley_pos,130,"T1 and T2")

        ax8.axis("off")

        st.pyplot(fig8)

        # =====================================================
        # STEP BY STEP SOLUTION
        # =====================================================

        st.subheader("Step By Step Analytical Solution")

        st.code(
            f"Fp = {T1} - {T2}"
        )

        st.code(
            f"Fp = {round(Fp,2)} N"
        )

        st.code(
            f"T = (9550 * {P} * 1000) / {N}"
        )

        st.code(
            f"T = {round(T,2)} N-mm"
        )

        st.code(
            f"M = (({Fg} + {round(Fp,2)}) * {L}) / 4"
        )

        st.code(
            f"M = {round(M,2)} N-mm"
        )

        st.code(
            f"Te = sqrt(({round(M,2)}^2) + ({round(T,2)}^2))"
        )

        st.code(
            f"Te = {round(Te,2)} N-mm"
        )

        st.code(
            f"d = ((16 * {round(Te,2)}) / "
            f"(3.14 * {tau}))^(1/3)"
        )

        st.code(
            f"d = {round(d,2)} mm"
        )

        st.code(
            "Formula Used:"
        )

        st.code(
            "Fp = T1 - T2"
        )

        st.code(
            "T = (9550 * P * 1000) / N"
        )

        st.code(
            "M = ((Fg + Fp) * L) / 4"
        )

        st.code(
            "Te = sqrt(M^2 + T^2)"
        )

        st.code(
            "d = ((16 * Te) / (pi * tau))^(1/3)"
        )

        # =====================================================
        # PDF REPORT
        # =====================================================

        pdf_buffer = BytesIO()

        doc = SimpleDocTemplate(pdf_buffer)

        elements = []

        elements.append(
            Paragraph(
                "Gear + Pulley Shaft Report",
                styles['Title']
            )
        )

        elements.append(Spacer(1,20))

        elements.append(
            Paragraph(
                f"Power = {P}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Speed = {N}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Gear Force = {Fg}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"T1 = {T1}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"T2 = {T2}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Length = {L}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Stress = {tau}",
                styles['BodyText']
            )
        )

        # =====================================================
        # SHAFT IMAGE
        # =====================================================

        temp7 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig7.savefig(temp7.name)

        elements.append(
            Image(
                temp7.name,
                width=400,
                height=120
            )
        )

        # =====================================================
        # 3D IMAGE
        # =====================================================

        temp3d = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig3d.savefig(temp3d.name)

        elements.append(
            Image(
                temp3d.name,
                width=400,
                height=150
            )
        )

        # =====================================================
        # FBD IMAGE
        # =====================================================

        temp8 = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        )

        fig8.savefig(temp8.name)

        elements.append(
            Image(
                temp8.name,
                width=400,
                height=120
            )
        )

        # =====================================================
        # PDF CALCULATIONS
        # =====================================================

        elements.append(
            Paragraph(
                "Step By Step Calculations",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                f"Fp = {T1} - {T2}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Fp = {round(Fp,2)} N",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"T = (9550 * {P} * 1000) / {N}",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"T = {round(T,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"M = (({Fg} + {round(Fp,2)}) * {L}) / 4",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"M = {round(M,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Te = sqrt(({round(M,2)}^2) + ({round(T,2)}^2))",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"Te = {round(Te,2)} N-mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = ((16 * {round(Te,2)}) / "
                f"(3.14 * {tau}))^(1/3)",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                f"d = {round(d,2)} mm",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "Formula Used:",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                "Fp = T1 - T2",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "T = (9550 * P * 1000) / N",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "M = ((Fg + Fp) * L) / 4",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "Te = sqrt(M^2 + T^2)",
                styles['BodyText']
            )
        )

        elements.append(
            Paragraph(
                "d = ((16 * Te) / (pi * tau))^(1/3)",
                styles['BodyText']
            )
        )

        doc.build(elements)

        pdf_buffer.seek(0)

        st.download_button(
            "Download Full PDF Report",
            data=pdf_buffer,
            file_name="gear_pulley_shaft_report.pdf",
            mime="application/pdf" 
)
