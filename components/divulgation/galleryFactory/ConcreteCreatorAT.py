from components.divulgation.galleryFactory.GalleryCreator import GalleryCreator
from components.divulgation.galleryFactory.Product import Product
from components.divulgation.galleryFactory.ConcreteAT import ConcreteAT

class ConcreteCreatorAT(GalleryCreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Product:
        return ConcreteAT()