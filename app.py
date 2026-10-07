import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Generative Fireworks", layout="centered")

st.title("🎆 Generative Fireworks")
st.write("A generative poster developed through four stages: Simple, Preset Style, Interactive, and 3D-like.")

stage = st.selectbox(
    "Choose a stage",
    ["Simple", "Preset Style", "Interactive", "3D-like"]
)

def setup():
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    return fig, ax

def simple():
    fig, ax = setup()
    cx, cy = 0, 0
    for angle in np.linspace(0, 2*np.pi, 24, endpoint=False):
        length = np.random.uniform(1.5, 3.5)
        x = [cx, cx + length*np.cos(angle)]
        y = [cy, cy + length*np.sin(angle)]
        ax.plot(x, y, linewidth=1.5)
    ax.scatter(cx, cy, s=20)
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_aspect("equal"); ax.axis("off")
    return fig

def preset_style():
    fig, ax = setup()
    cx, cy = 0, 0
    for angle in np.linspace(0, 2*np.pi, 36, endpoint=False):
        length = np.random.uniform(1.5, 3.5)
        t = np.linspace(0, 1, 30)
        x = cx + length*t*np.cos(angle)
        y = cy + length*t*np.sin(angle)
        x += np.random.normal(0, 0.03, len(x))
        y += np.random.normal(0, 0.03, len(y))
        ax.plot(x, y,
                linewidth=np.random.uniform(0.5, 2.0),
                alpha=np.random.uniform(0.4, 0.9))
    for _ in range(120):
        angle = np.random.uniform(0, 2*np.pi)
        distance = np.random.uniform(1.0, 3.8)
        x = cx + distance*np.cos(angle)
        y = cy + distance*np.sin(angle)
        ax.scatter(x, y,
                   s=np.random.uniform(2, 15),
                   alpha=np.random.uniform(0.2, 0.8))
    ax.scatter(cx, cy, s=30)
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_aspect("equal"); ax.axis("off")
    return fig

def draw_firework(ax, cx, cy, size, alpha, rays=32):
    for angle in np.linspace(0, 2*np.pi, rays, endpoint=False):
        length = np.random.uniform(size*0.7, size)
        t = np.linspace(0, 1, 35)
        curve = np.sin(t*np.pi)*np.random.uniform(-0.15, 0.15)
        x = cx + length*t*np.cos(angle)
        y = cy + length*t*np.sin(angle)
        x += curve*np.sin(angle)
        y += curve*np.cos(angle)
        ax.plot(x, y,
                linewidth=np.random.uniform(0.5, 1.8),
                alpha=alpha)
    for _ in range(int(size*35)):
        angle = np.random.uniform(0, 2*np.pi)
        distance = np.random.uniform(size*0.5, size*1.2)
        x = cx + distance*np.cos(angle)
        y = cy + distance*np.sin(angle)
        ax.scatter(x, y,
                   s=np.random.uniform(2, 12),
                   alpha=alpha*np.random.uniform(0.3, 0.8))
    ax.scatter(cx, cy, s=size*8, alpha=alpha)

def interactive():
    count = st.slider("Number of fireworks", 1, 8, 3)
    size = st.slider("Firework size", 1.0, 4.0, 2.5, 0.5)
    particles = st.slider("Particle count", 20, 150, 80, 10)

    fig, ax = setup()
    for _ in range(count):
        cx = np.random.uniform(-3, 3)
        cy = np.random.uniform(-3, 3)

        for angle in np.linspace(0, 2*np.pi, 30, endpoint=False):
            length = np.random.uniform(size*0.5, size)
            t = np.linspace(0, 1, 25)
            x = cx + length*t*np.cos(angle)
            y = cy + length*t*np.sin(angle)
            x += np.random.normal(0, 0.03, len(x))
            y += np.random.normal(0, 0.03, len(y))
            ax.plot(x, y,
                    linewidth=np.random.uniform(0.5, 1.8),
                    alpha=np.random.uniform(0.4, 0.9))

        for _ in range(particles):
            angle = np.random.uniform(0, 2*np.pi)
            distance = np.random.uniform(size*0.4, size*1.2)
            x = cx + distance*np.cos(angle)
            y = cy + distance*np.sin(angle)
            ax.scatter(x, y,
                       s=np.random.uniform(2, 12),
                       alpha=np.random.uniform(0.2, 0.8))
        ax.scatter(cx, cy, s=25)

    ax.set_xlim(-5, 5); ax.set_ylim(-5, 5)
    ax.set_aspect("equal"); ax.axis("off")
    return fig

def three_d_like():
    fig, ax = setup()

    for _ in range(8):
        draw_firework(ax,
                      np.random.uniform(-7, 7),
                      np.random.uniform(-2, 4),
                      np.random.uniform(0.7, 1.3),
                      np.random.uniform(0.15, 0.35))

    for _ in range(5):
        draw_firework(ax,
                      np.random.uniform(-6, 6),
                      np.random.uniform(-2, 4),
                      np.random.uniform(1.3, 2.0),
                      np.random.uniform(0.4, 0.65))

    for _ in range(3):
        draw_firework(ax,
                      np.random.uniform(-5, 5),
                      np.random.uniform(-1, 4),
                      np.random.uniform(2.2, 3.2),
                      np.random.uniform(0.7, 1.0))

    ax.set_xlim(-9, 9); ax.set_ylim(-4, 7)
    ax.set_aspect("equal"); ax.axis("off")
    return fig

if stage == "Simple":
    fig = simple()
elif stage == "Preset Style":
    fig = preset_style()
elif stage == "Interactive":
    fig = interactive()
else:
    fig = three_d_like()

st.pyplot(fig)
