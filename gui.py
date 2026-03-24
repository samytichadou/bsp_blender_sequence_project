import bpy


class BSP_PT_strip_infos(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "strip"
    bl_label = "BSP"

    @classmethod
    def poll(cls, context):
        strip = context.active_strip
        if not strip:
            return False
        if strip.type=="SCENE":
            return True
        elif strip.type=='IMAGE':
            return strip.bsp_properties.is_bsp

    def draw(self, context):
        strip = context.active_strip
        props = strip.bsp_properties

        layout = self.layout
        if strip.type=="SCENE":
            layout.prop(props, "is_bsp")
        layout.prop(props, "external_filepath")
        layout.prop(props, "scene_name")

### REGISTER ---
def register():
    bpy.utils.register_class(BSP_PT_strip_infos)

def unregister():
    bpy.utils.unregister_class(BSP_PT_strip_infos)
