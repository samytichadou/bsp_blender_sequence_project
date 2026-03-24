import bpy

def callback_scene_selection(self, context):
    if self.target_scene == context.sequencer_scene:
        print("BSP --- BSP scene has to be different from sequence scene")
        self.target_scene = None

class BSP_PR_strip_properties(bpy.types.PropertyGroup):
    is_bsp : bpy.props.BoolProperty(
        name="BSP Strip",
    )
    target_scene: bpy.props.PointerProperty(
        name="Scene",
        type = bpy.types.Scene,
        update = callback_scene_selection,
    )
    render_filepath: bpy.props.StringProperty(
        name="Render",
        subtype = "FILE_PATH",
    )

class BSP_PR_origin_scene(bpy.types.PropertyGroup):
    scene_name : bpy.props.StringProperty()
    scene_path : bpy.props.StringProperty()
    workspace_name : bpy.props.StringProperty()

### REGISTER ---
def register():
    bpy.utils.register_class(BSP_PR_strip_properties)
    bpy.utils.register_class(BSP_PR_origin_scene)

    bpy.types.SceneStrip.bsp_properties = \
        bpy.props.PointerProperty(type = BSP_PR_strip_properties, name="BSP")
    bpy.types.ImageStrip.bsp_properties = \
        bpy.props.PointerProperty(type = BSP_PR_strip_properties, name="BSP")
    bpy.types.WindowManager.bsp_origin_scene = \
        bpy.props.PointerProperty(type = BSP_PR_origin_scene)

def unregister():
    bpy.utils.unregister_class(BSP_PR_strip_properties)
    bpy.utils.unregister_class(BSP_PR_origin_scene)

    del bpy.types.SceneStrip.bsp_properties
    del bpy.types.ImageStrip.bsp_properties
    del bpy.types.WindowManager.bsp_origin_scene
