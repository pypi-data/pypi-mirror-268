from absl import flags,logging,app
import enum
@enum.unique
class ModelsToRelax(enum.Enum):
  ALL = 0
  BEST = 1
  NONE = 2
 
flags.DEFINE_enum_class('models_to_relax', ModelsToRelax.NONE, ModelsToRelax,"models to relax")
flags.DEFINE_boolean("remove_pickles", False, "whether to remove pickles. Default is False")
FLAGS = flags.FLAGS

def main(args):
  logging.info(f"models to relax is :{FLAGS.models_to_relax}")

if __name__ == "__main__":
  app.run(main)