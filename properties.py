import bpy


class BSP_PR_strip_properties(bpy.types.PropertyGroup):
    is_bsp : bpy.props.BoolProperty(
        name="BSP Strip",
    )
    external_filepath: bpy.props.StringProperty(
        name="External Blender File",
        subtype = "FILE_PATH",
    )
    scene_name: bpy.props.StringProperty(
        name="Scene Name",
    )
    end_action: bpy.props.EnumProperty(
        name = "End Action",
        default = 'PLAY',
        items = (
        ('PLAY', "Play Video", ""),
        ('NOTHING', "Do Nothing", ""),
        ),
    )
    

### REGISTER ---
def register():
    bpy.utils.register_class(BSP_PR_strip_properties)
    bpy.types.SceneStrip.bsp_properties = \
        bpy.props.PointerProperty(type = BSP_PR_strip_properties, name="BSP")
    bpy.types.ImageStrip.bsp_properties = \
        bpy.props.PointerProperty(type = BSP_PR_strip_properties, name="BSP")

def unregister():
    bpy.utils.unregister_class(BSP_PR_strip_properties)
    del bpy.types.SceneStrip.bsp_properties
    del bpy.types.ImageStrip.bsp_properties
