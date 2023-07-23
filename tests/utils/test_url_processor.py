from src.utils.url_processor import join_url, get_url_resource_name


class TestUrlJoin:
    def test_url_join_without_slash(self):
        mock_base_url = "base_url"
        mock_relative_url = "relative_url"

        join_url_result = join_url(
            base_url=mock_base_url, relative_url=mock_relative_url
        )
        assert join_url_result == "base_url/relative_url"

    def test_url_join_base_url_with_trailing_slash(self):
        mock_base_url = "base_url/"
        mock_relative_url = "relative_url"

        join_url_result = join_url(
            base_url=mock_base_url, relative_url=mock_relative_url
        )
        assert join_url_result == "base_url/relative_url"

    def test_url_join_relative_url_with_leading_slash(self):
        mock_base_url = "base_url"
        mock_relative_url = "/relative_url"

        join_url_result = join_url(
            base_url=mock_base_url, relative_url=mock_relative_url
        )
        assert join_url_result == "base_url/relative_url"

    def test_url_join_base_url_with_trailing_slash_and_relative_url_with_leading_slash(
        self,
    ):
        mock_base_url = "base_url/"
        mock_relative_url = "/relative_url"

        join_url_result = join_url(
            base_url=mock_base_url, relative_url=mock_relative_url
        )
        assert join_url_result == "base_url/relative_url"


class TestGetUrlResourceName:
    def test_get_url_resource_name_double_layer(self):
        mock_url = "layer1/resource"

        get_url_resource_name_result = get_url_resource_name(url=mock_url)
        assert get_url_resource_name_result == "resource"

    def test_get_url_resource_name_triple_layer(self):
        mock_url = "layer1/layer2/resource"

        get_url_resource_name_result = get_url_resource_name(url=mock_url)
        assert get_url_resource_name_result == "resource"
