import bpy


class BSP_PRF_addonpreferences(bpy.types.AddonPreferences) :
    bl_idname = __package__

    playblast_folderpath : bpy.props.StringProperty(
            name = "Playblast Path",
            default = "",
            description = "Folder where temporary Playblast are stored",
            subtype = "DIR_PATH"
            )

    def draw(self, context) :
        layout = self.layout
        layout.prop(self, "playblast_folderpath")


# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(__package__)
    return getattr(addon, "preferences", None)


### REGISTER ---
def register():
    bpy.utils.register_class(BSP_PRF_addonpreferences)

def unregister():
    bpy.utils.unregister_class(BSP_PRF_addonpreferences)
