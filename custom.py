# custom.py - put this file in the ROOT of the Godot source folder (next to SConstruct).
# SCons reads it automatically. Anything passed on the command line overrides it.
# Unknown option names only print a warning, they never stop the build.
#
# Built for: Island Fight Race (Godot 4.7, GL Compatibility, Jolt, Playgama bridge,
# single-thread web export, no GDExtension).  Every line below was checked against
# your project files (scenes, scripts, imports, export preset).

# ---------- size / speed (main reason the other agents' build was 23 MB) ----------
optimize = "size"
lto = "full"
debug_symbols = False
separate_debug_symbols = False
dev_build = False
disable_exceptions = True
# Your current template was compiled much tighter (-Oz). -Os let LTO inline too much (93 huge functions vs 49).
ccflags = "-Oz"
linkflags = "-Oz"

# ---------- web settings that MUST match your export preset ----------
threads = False                # preset: thread_support=false
dlink_enabled = False          # preset: extensions_support=false
javascript_eval = True         # KEEP: Playgama bridge uses JavaScriptBridge ~100 times

# ---------- engine feature switches ----------
disable_xr = True
disable_navigation_2d = True
disable_navigation_3d = True
disable_physics_2d = True      # game uses only 3D physics (Jolt)
# NOT disabled on purpose: disable_3d (game is 3D), disable_advanced_gui (game uses
# FileDialog, ItemList, TextEdit, RichTextLabel, PopupMenu), deprecated (see README).

# ---------- modules: OFF (game does not use them) ----------
module_openxr_enabled = False
module_webxr_enabled = False
module_mobile_vr_enabled = False
module_navigation_2d_enabled = False
module_navigation_3d_enabled = False
module_csg_enabled = False
module_gridmap_enabled = False
module_enet_enabled = False
module_webrtc_enabled = False
module_upnp_enabled = False
module_jsonrpc_enabled = False
module_multiplayer_enabled = False
module_camera_enabled = False
module_theora_enabled = False          # no .ogv video
module_minimp3_enabled = False         # only .wav and one .ogg are used (name in older Godot)
module_mp3_enabled = False             # same module, name used by Godot 4.7
module_visual_shader_enabled = False   # game uses no VisualShader
module_ktx_enabled = False             # needs basis_universal; not used
module_tinyexr_enabled = False         # .exr files are imported at edit time, not loaded at runtime
module_regex_enabled = False
module_noise_enabled = False
module_gltf_enabled = False            # .glb is converted to .scn on export
module_fbx_enabled = False
module_basis_universal_enabled = False # no Basis Universal textures (all imports are mode 0 or 2)
module_interactive_music_enabled = False
module_lightmapper_rd_enabled = False  # baking is editor-only; baked lightmaps still render
module_raycast_enabled = False
module_vhacd_enabled = False
module_xatlas_unwrap_enabled = False
module_godot_physics_2d_enabled = False
module_godot_physics_3d_enabled = False  # project setting is "Jolt Physics"
module_text_server_adv_enabled = False   # fallback server is what you use now

# ---------- modules: KEPT on purpose (game needs them) ----------
module_text_server_fb_enabled = True    # REQUIRED: my last build had no text server (no text would be drawn)
module_freetype_enabled = True
# gdscript (compressed scripts), jolt_physics, text_server_fb, freetype, brotli (default font is woff2),
# msdfgen left at default on purpose: I switched it off last time and the text server vanished
# svg (default UI icons for CheckButton/OptionButton/HSlider), jpg + webp (profile photo via Image.load),
# websocket + mbedtls (WebSocketPeer, HTTPRequest, Crypto over TLS), ogg + vorbis (loop.ogg),
# astcenc/etcpak/cvtt/bcdec/bmp/tga/dds/hdr (small, texture fallback safety)
