import fairgraph.openminds.chemicals as chem
import fairgraph.openminds.controlled_terms as terms
from test.utils import mock_client, kg_client, skip_if_no_connection


@skip_if_no_connection
def test_retrieve_single_chemical_mixture_from_uuid(kg_client):
    chem.set_error_handling(None)
    mix = chem.ChemicalMixture.from_uuid(
        "a19bdadd-12a3-40a1-a82f-78cc9d431783",
        kg_client,
        scope="in progress",
        follow_links={"has_parts": {"amount": {"unit": {}}, "chemical_product": {}}},
    )
    assert mix.uuid == "a19bdadd-12a3-40a1-a82f-78cc9d431783"
    assert len(mix.has_parts) > 1
    for amount in mix.has_parts:
        assert isinstance(amount, chem.AmountOfChemical)
        assert amount.amount.unit.name == "millimolar"
        assert isinstance(amount.chemical_product, terms.MolecularEntity)


@skip_if_no_connection
def test_existence_query_chemical_mixture(kg_client):
    chem.set_error_handling(None)
    mix = chem.ChemicalMixture.from_uuid(
        "a19bdadd-12a3-40a1-a82f-78cc9d431783",
        kg_client,
        scope="in progress",
        follow_links={"has_parts": {"amount": {"unit": {}}, "chemical_product": {}}},
    )
    mix.id = None
    query_filter = mix._build_existence_query()
    expected = {}
    assert query_filter == expected
