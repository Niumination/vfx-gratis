"""
HUMAN-001 - Awakening Protocol
Blender Scene Setup Script with HDRI Integration

Phase 1: Data Stream - Particle system
Phase 2: Energy Core - Energy burst  
Phase 3: Neural Boot - Neural network
Phase 4: Limb Activation - Servo glow
Phase 5: Diagnostics - HUD
Phase 6: Awakening Complete - Energy surge

This is a production-ready scene setup script for VFX creation with HDRI.
"""

import bpy
import math
import random

# Create new scene
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.name = "HUMAN_001_Awakening"

# Set render engine to Cycles (VFX quality)
scene.render.engine = 'CYCLES'
scene.cycles.samples = 64
scene.cycles.use_denoising = True

# Set resolution
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Set frame range
scene.frame_start = 1
scene.frame_end = 120

# World setup - dark studio with HDRI
world = bpy.data.worlds.new("AwakeningWorld")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.01, 0.01, 0.02, 1.0)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0

print("HUMAN_001 SCENE_SETUP_COMPLETE")
print("ENGINE:", scene.render.engine)
print("RESOLUTION:", scene.render.resolution_x, "x", scene.render.resolution_y)
print("FRAMES:", scene.frame_start, "-", scene.frame_end)
print("WORLD:", scene.world.name)

# Create HDRI world nodes properly for Blender 4.0
# Clear existing nodes
world.node_tree.nodes.clear()
world.use_nodes = True

# Add Background node
bg = world.node_tree.nodes.new(type='ShaderNodeBackground')
bg.inputs[0].default_value = (0.01, 0.01, 0.02, 1.0)
bg.inputs[1].default_value = 1.0

# Add World Output node
output = world.node_tree.nodes.new(type='ShaderNodeOutputWorld')
world.node_tree.links.new(bg.outputs[0], output.inputs[0])

# Add Image Texture node for HDRI
img = world.node_tree.nodes.new(type='ShaderNodeTexEnvironment')
img.image = bpy.data.images.load("/tmp/vfx-gratis-clone/assets/hdri/StinsonBeach.hdr")

# Link
world.node_tree.links.new(img.outputs[0], bg.inputs[0])

print("HDRI_SETUP_COMPLETE: StinsonBeach.hdr")
print("HUMAN_001_SCENE_READY")

# Save scene
bpy.ops.wm.save_as_mainfile(filepath="/tmp/vfx-gratis-clone/projects/vfx-001/humanoid_awakening.blend")
print("SCENE_SAVED: /tmp/vfx-gratis-clone/projects/vfx-001/humanoid_awakening.blend")
